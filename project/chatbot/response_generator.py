import random
import os
import time
import logging
from typing import Dict, List
from chatbot.training_data import RESPONSES, SUGGESTIONS, COLLEGE_INFO

# Configure logging for AI service monitoring
ai_logger = logging.getLogger('ai_services')

# Import AI services
try:
    from openai import OpenAI
    import google.generativeai as genai
    import requests
    import json
    from dotenv import load_dotenv
    AI_SERVICES_AVAILABLE = True
except ImportError:
    AI_SERVICES_AVAILABLE = False
    print("Warning: AI services not available. Install openai, google-generativeai, and requests packages.")

class ResponseGenerator:
    """Generate appropriate responses based on classified intents."""
    
    def __init__(self):
        self.responses = RESPONSES
        self.suggestions = SUGGESTIONS
        self.college_info = COLLEGE_INFO
        
        # Initialize AI services if available
        if AI_SERVICES_AVAILABLE:
            # Load environment variables from .env if present
            try:
                load_dotenv()
            except Exception:
                pass
            self._setup_ai_services()
    
    def _setup_ai_services(self):
        """Setup AI services with API keys."""
        try:
            # Get API keys from environment variables
            openai_api_key = os.environ.get("OPENAI_API_KEY")
            google_api_key = os.environ.get("GOOGLE_API_KEY")
            perplexity_api_key = os.environ.get("PERPLEXITY_API_KEY")
            
            # Store API keys for later use
            self.openai_api_key = openai_api_key
            self.google_api_key = google_api_key
            self.perplexity_api_key = perplexity_api_key
            
            # Configure Google Gemini
            if google_api_key:
                genai.configure(api_key=google_api_key)
                print("Google Gemini AI configured")
            else:
                print("Google API key not found in environment variables")
            
            # Check OpenAI configuration
            if openai_api_key:
                print("OpenAI API key found")
            else:
                print("OpenAI API key not found in environment variables")
                print("   Set OPENAI_API_KEY environment variable for ChatGPT access")
            
            # Check Perplexity configuration
            if perplexity_api_key:
                print("Perplexity API key found")
            else:
                print("Perplexity API key not found in environment variables")
                print("   Set PERPLEXITY_API_KEY environment variable for Perplexity AI access")
            
            self.ai_services_configured = True
            print("AI services setup completed - ChatGPT, Gemini, and Perplexity will be attempted")
            
        except Exception as e:
            print(f"Error setting up AI services: {e}")
            self.ai_services_configured = False
    
    def _format_response(self, response_template: str) -> str:
        """Format the response template with college information."""
        try:
            # Ensure all required keys are present before formatting
            info = {key: self.college_info.get(key, f"[{key.upper()}_INFO_MISSING]") for key in self.college_info}
            
            # Flatten nested dictionaries for easier formatting
            admissions_info = info.get('admissions', {})
            fees_info = info.get('fees', {})

            return response_template.format(
                name=info.get('name'),
                established=info.get('established'),
                location=info.get('location'),
                accreditation=info.get('accreditation'),
                ranking=info.get('ranking'),
                student_count=info.get('student_count'),
                faculty_count=info.get('faculty_count'),
                campus_size=info.get('campus_size'),
                admissions=admissions_info,
                fees=fees_info,
                departments=', '.join(info.get('departments', []))
            )
        except (KeyError, TypeError) as e:
            # Log the error for debugging
            print(f"Error formatting response: {e}")
            return "Sorry, I'm having trouble retrieving the information right now."
    
    def _fallback_to_ai(self, user_message: str) -> str:
        """Fallback to AI services when local data doesn't have the answer."""
        if not AI_SERVICES_AVAILABLE:
            return "I'm sorry, I don't have information about that topic in my knowledge base, and I'm unable to connect to external AI services right now. Please contact our admissions office for more specific information."
        
        # Create a context-aware prompt for college-related questions
        context_prompt = f"""You are a helpful assistant for RGM College of Engineering and Technology. 
        A student is asking: "{user_message}"
        
        Please provide a helpful, accurate response about college-related topics. If the question is not about college, education, or academic matters, politely redirect them to ask about college-related topics.
        
        Keep your response concise, friendly, and informative. If you don't know specific details about RGM College, provide general guidance about the topic."""
        
        # Try multiple AI services in order of preference
        ai_services = [
            ("Gemini", self._try_gemini),
            ("ChatGPT", self._try_chatgpt),
            ("Perplexity", self._try_perplexity)
        ]
        
        for service_name, service_func in ai_services:
            try:
                response = self._retry_ai_service(service_func, context_prompt, service_name)
                if response and response.strip():
                    print(f"Successfully got response from {service_name}")
                    ai_logger.info(f"AI service {service_name} responded successfully for query: {user_message[:50]}...")
                    return response
            except Exception as e:
                print(f"{service_name} API failed with error: {e}")
                ai_logger.error(f"AI service {service_name} failed for query: {user_message[:50]}... Error: {str(e)}")
                continue
        
        # If all AI services fail, return a helpful fallback message
        return "I'm sorry, I'm having trouble connecting to my knowledge base right now. Please try again later or contact our admissions office directly for assistance."
    
    def _retry_ai_service(self, service_func, prompt: str, service_name: str, max_retries: int = 2) -> str:
        """Retry AI service calls with exponential backoff."""
        for attempt in range(max_retries + 1):
            try:
                response = service_func(prompt)
                if response and response.strip():
                    return response
                elif attempt < max_retries:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    print(f"{service_name} returned empty response, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception(f"Empty response after {max_retries + 1} attempts")
            except Exception as e:
                if attempt < max_retries:
                    wait_time = 2 ** attempt
                    print(f"{service_name} failed (attempt {attempt + 1}), retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise e
    
    def _try_gemini(self, prompt: str) -> str:
        """Try to get response from Google Gemini AI."""
        try:
            # Try different Gemini models (using current model names)
            models_to_try = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
            
            for model_name in models_to_try:
                try:
                    gemini_model = genai.GenerativeModel(model_name)
                    response = gemini_model.generate_content(prompt)
                    if response and response.text:
                        return response.text
                except Exception as e:
                    print(f"Gemini model {model_name} failed: {e}")
                    continue
            
            raise Exception("All Gemini models failed")
        except Exception as e:
            raise Exception(f"Gemini API error: {e}")
    
    def _try_chatgpt(self, prompt: str) -> str:
        """Try to get response from OpenAI ChatGPT."""
        try:
            # Try with API key if available
            if hasattr(self, 'openai_api_key') and self.openai_api_key:
                client = OpenAI(api_key=self.openai_api_key)
            else:
                # Try without explicit API key (uses environment variable or .env)
                client = OpenAI()
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7
            )
            
            if response and response.choices and response.choices[0].message.content:
                return response.choices[0].message.content
            else:
                raise Exception("Empty response from ChatGPT")
                
        except Exception as e:
            raise Exception(f"ChatGPT API error: {e}")
    
    def _try_perplexity(self, prompt: str) -> str:
        """Try to get response from Perplexity AI."""
        try:
            if not hasattr(self, 'perplexity_api_key') or not self.perplexity_api_key:
                raise Exception("Perplexity API key not configured")
            
            headers = {
                "Authorization": f"Bearer {self.perplexity_api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "llama-3.1-sonar-small-128k-online",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful assistant for RGM College of Engineering and Technology. Provide accurate, helpful responses about college-related topics. Keep responses concise and informative."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }
            
            response = requests.post(
                "https://api.perplexity.ai/chat/completions",
                headers=headers,
                json=data,
                timeout=15  # Reduced timeout for better responsiveness
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('choices') and result['choices'][0].get('message'):
                    return result['choices'][0]['message']['content']
                else:
                    raise Exception("Invalid response format from Perplexity")
            else:
                raise Exception(f"Perplexity API returned status {response.status_code}: {response.text}")
                
        except Exception as e:
            raise Exception(f"Perplexity API error: {e}")

    def generate_response(self, intent_result: Dict, processed_input: Dict, session_id: str) -> Dict:
        """Generate an appropriate response based on the classified intent."""
        intent = intent_result.get('intent', 'unknown')
        confidence = intent_result.get('confidence', 0.0)
        user_message = processed_input.get('original_text', '')
        
        # Smart AI fallback logic - use AI for complex queries, low confidence, or unknown intents
        should_use_ai = (
            confidence < 0.6 or  # Lower threshold to use more local responses
            intent == 'unknown' or  # Unknown intent
            len(user_message.split()) > 20 or  # Very complex queries only
            any(keyword in user_message.lower() for keyword in [
                'compare', 'difference', 'vs', 'versus', 'which is better',
                'pros and cons', 'advantages', 'disadvantages', 'explain',
                'how does', 'what if', 'why', 'when should', 'where can',
                'latest trends', 'current market', 'analysis', 'research'
            ])  # Complex question patterns
        )
        
        if should_use_ai:
            print(f"🤖 Attempting AI fallback - Confidence: {confidence:.2f}, Intent: {intent}")
            ai_response = self._fallback_to_ai(user_message)
            if ai_response and not ai_response.startswith("I'm sorry, I don't have information"):
                return {
                    'response': ai_response,
                    'suggestions': [
                        "Tell me about admissions",
                        "What courses do you offer?",
                        "What are the fees?",
                        "Show me campus facilities"
                    ],
                    'confidence': 0.9,  # High confidence for AI responses
                    'intent': 'ai_fallback',
                    'source': 'ai'
                }
        
        # Use local responses for high confidence matches
        response_templates = self.responses.get(intent, self.responses['unknown'])
        base_response_template = random.choice(response_templates)
        
        # Format the response with dynamic data
        final_response = self._format_response(base_response_template)
        
        # Get relevant suggestions
        suggestions = self.suggestions.get(intent, self.suggestions.get('default', []))
        
        return {
            'response': final_response,
            'suggestions': random.sample(suggestions, min(3, len(suggestions))),
            'confidence': confidence,
            'intent': intent,
            'source': 'local'
        }