#!/usr/bin/env python3
"""
Setup script to help configure API keys for AI services.
"""

import os
import sys

def setup_api_keys():
    """Interactive setup for API keys."""
    print("🔑 AI Services API Key Setup")
    print("=" * 40)
    print()
    
    # Check current environment
    openai_key = os.environ.get("OPENAI_API_KEY")
    google_key = os.environ.get("GOOGLE_API_KEY")
    perplexity_key = os.environ.get("PERPLEXITY_API_KEY")
    
    print("Current API Key Status:")
    print(f"OpenAI API Key: {'✅ Set' if openai_key else '❌ Not Set'}")
    print(f"Google API Key: {'✅ Set' if google_key else '❌ Not Set'}")
    print(f"Perplexity API Key: {'✅ Set' if perplexity_key else '❌ Not Set'}")
    print()
    
    if not openai_key:
        print("📝 To set up OpenAI API Key:")
        print("1. Visit: https://platform.openai.com/api-keys")
        print("2. Create an account and generate an API key")
        print("3. Set the environment variable:")
        print("   Windows: set OPENAI_API_KEY=your_key_here")
        print("   Linux/Mac: export OPENAI_API_KEY=your_key_here")
        print()
    
    if not google_key:
        print("📝 To set up Google API Key:")
        print("1. Visit: https://makersuite.google.com/app/apikey")
        print("2. Create an account and generate an API key")
        print("3. Set the environment variable:")
        print("   Windows: set GOOGLE_API_KEY=your_key_here")
        print("   Linux/Mac: export GOOGLE_API_KEY=your_key_here")
        print()
    
    if not perplexity_key:
        print("📝 To set up Perplexity API Key:")
        print("1. Visit: https://www.perplexity.ai/settings/api")
        print("2. Create an account and generate an API key")
        print("3. Set the environment variable:")
        print("   Windows: set PERPLEXITY_API_KEY=your_key_here")
        print("   Linux/Mac: export PERPLEXITY_API_KEY=your_key_here")
        print()
    
    # Interactive setup
    if input("Would you like to set API keys now? (y/n): ").lower() == 'y':
        if not openai_key:
            openai_key = input("Enter your OpenAI API Key: ").strip()
            if openai_key:
                os.environ["OPENAI_API_KEY"] = openai_key
                print("✅ OpenAI API Key set for this session")
        
        if not google_key:
            google_key = input("Enter your Google API Key: ").strip()
            if google_key:
                os.environ["GOOGLE_API_KEY"] = google_key
                print("✅ Google API Key set for this session")
        
        if not perplexity_key:
            perplexity_key = input("Enter your Perplexity API Key: ").strip()
            if perplexity_key:
                os.environ["PERPLEXITY_API_KEY"] = perplexity_key
                print("✅ Perplexity API Key set for this session")
    
    print()
    print("🚀 Your chatbot is now configured to use ChatGPT, Gemini AI, and Perplexity!")
    print("   - Questions not in local data will be answered by AI services")
    print("   - The system will try Gemini first, then ChatGPT, then Perplexity as fallbacks")
    print("   - If all AI services fail, it will use local responses")

def test_ai_connection():
    """Test AI service connections."""
    print("\n🧪 Testing AI Service Connections...")
    print("-" * 40)
    
    try:
        from chatbot.response_generator import ResponseGenerator
        
        # Initialize response generator
        response_generator = ResponseGenerator()
        
        # Test with a simple question
        test_question = "What is artificial intelligence?"
        intent_result = {'intent': 'unknown', 'confidence': 0.3}
        processed_input = {'original_text': test_question}
        
        print(f"Testing with: {test_question}")
        response_data = response_generator.generate_response(
            intent_result, processed_input, 'test_session'
        )
        
        print(f"Response source: {response_data.get('source', 'unknown')}")
        print(f"Response preview: {response_data['response'][:100]}...")
        
        if response_data.get('source') == 'ai':
            print("✅ AI services are working correctly!")
        else:
            print("⚠️  Using local responses (AI services may not be configured)")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    setup_api_keys()
    test_ai_connection()

