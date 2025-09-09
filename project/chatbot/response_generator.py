import random
from typing import Dict, List
from chatbot.training_data import RESPONSES, SUGGESTIONS, COLLEGE_INFO

class ResponseGenerator:
    """Generate appropriate responses based on classified intents."""
    
    def __init__(self):
        self.responses = RESPONSES
        self.suggestions = SUGGESTIONS
        self.college_info = COLLEGE_INFO
    
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

    def generate_response(self, intent_result: Dict, processed_input: Dict, session_id: str) -> Dict:
        """Generate an appropriate response based on the classified intent."""
        intent = intent_result.get('intent', 'unknown')
        confidence = intent_result.get('confidence', 0.0)
        
        # Select a response template
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
            'intent': intent
        }