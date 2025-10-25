# 🤖 Hybrid College Enquiry Chatbot System

## Overview

Your chatbot system now features a **hybrid architecture** that intelligently combines local training data with external AI services (ChatGPT, Gemini AI, and Perplexity AI) to provide comprehensive responses to college-related queries.

## 🎯 How It Works

### 1. **Smart Response Selection**
- **High Confidence Local Responses**: When the system is confident (>80%) that it can answer from local training data, it uses predefined responses
- **AI Fallback**: For complex queries, low confidence matches, or unknown intents, the system automatically falls back to AI services
- **Multiple AI Services**: Tries Gemini AI first, then ChatGPT, then Perplexity AI as fallbacks

### 2. **Intelligent Query Processing**
The system uses sophisticated logic to determine when to use AI:
- Confidence score below 80%
- Unknown intent classification
- Complex queries (>15 words)
- Questions with comparison keywords ("compare", "vs", "advantages", "disadvantages")
- Analytical questions ("why", "how does", "what if", "explain")

### 3. **Robust Error Handling**
- Automatic retry mechanisms with exponential backoff
- Multiple AI service fallbacks
- Graceful degradation to local responses if all AI services fail

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys (Optional but Recommended)
```bash
python setup_api_keys.py
```

**API Key Sources:**
- **OpenAI (ChatGPT)**: https://platform.openai.com/api-keys
- **Google Gemini**: https://makersuite.google.com/app/apikey
- **Perplexity AI**: https://www.perplexity.ai/settings/api

### 3. Test the System
```bash
python test_hybrid_chatbot.py
```

### 4. Run the Chatbot
```bash
python app.py
```

## 🔧 Configuration

### Environment Variables
Set these environment variables for AI service access:

**Windows:**
```cmd
set OPENAI_API_KEY=your_openai_key_here
set GOOGLE_API_KEY=your_google_key_here
set PERPLEXITY_API_KEY=your_perplexity_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=your_openai_key_here
export GOOGLE_API_KEY=your_google_key_here
export PERPLEXITY_API_KEY=your_perplexity_key_here
```

## 📊 System Architecture

```
User Query
    ↓
NLP Processing
    ↓
Intent Classification
    ↓
Confidence Check
    ↓
┌─────────────────┬─────────────────┐
│ High Confidence │ Low Confidence  │
│ (>80%)          │ (<80%)          │
│                 │                 │
│ Local Response  │ AI Fallback     │
│ (Training Data) │ (Gemini →       │
│                 │  ChatGPT →      │
│                 │  Perplexity)    │
└─────────────────┴─────────────────┘
    ↓
Response Generation
    ↓
User Response
```

## 🧪 Testing

The system includes comprehensive testing capabilities:

### Test Categories
1. **Local Response Tests**: Verify training data responses work correctly
2. **AI Fallback Tests**: Ensure complex queries trigger AI responses
3. **API Connectivity Tests**: Check if AI services are properly configured

### Running Tests
```bash
python test_hybrid_chatbot.py
```

Expected output:
- ✅ Simple queries (greetings, basic info) → Local responses
- 🤖 Complex queries (comparisons, analysis) → AI responses

## 📝 Example Queries

### Local Responses (High Confidence)
- "Hello"
- "What courses do you offer?"
- "What are the admission requirements?"
- "Tell me about the fees"
- "What facilities are available?"

### AI Responses (Complex Queries)
- "What is artificial intelligence and how does it relate to computer science education?"
- "Compare the advantages and disadvantages of studying engineering vs medicine"
- "How does the job market look for computer science graduates in 2024?"
- "What are the latest trends in renewable energy engineering?"

## 🔍 Monitoring and Logging

The system includes comprehensive logging:
- AI service usage tracking
- Response source identification
- Error logging and retry attempts
- Performance monitoring

## 🛠️ Customization

### Adding New Training Data
Edit `chatbot/training_data.py` to add:
- New intent categories
- Additional example queries
- Response templates
- College-specific information

### Modifying AI Fallback Logic
Edit the confidence thresholds in `chatbot/response_generator.py`:
```python
should_use_ai = (
    confidence < 0.8 or  # Adjust this threshold
    intent == 'unknown' or
    # Add your custom logic here
)
```

### Adding New AI Services
1. Add the service configuration in `_setup_ai_services()`
2. Implement the service method (e.g., `_try_new_service()`)
3. Add it to the `ai_services` list in `_fallback_to_ai()`

## 🚨 Troubleshooting

### Common Issues

1. **No AI responses**: Check API keys are set correctly
2. **Slow responses**: AI services may be experiencing delays
3. **Empty responses**: Check internet connectivity and API quotas

### Debug Mode
Enable detailed logging by setting:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance Features

- **Retry Mechanisms**: Automatic retries with exponential backoff
- **Timeout Handling**: Prevents hanging on slow AI services
- **Caching**: Local responses are cached for faster subsequent queries
- **Fallback Chain**: Multiple AI services ensure high availability

## 🎉 Benefits

1. **Comprehensive Coverage**: Handles both simple and complex queries
2. **High Reliability**: Multiple fallback mechanisms
3. **Cost Effective**: Uses local data when possible, AI only when needed
4. **Scalable**: Easy to add new AI services or training data
5. **User-Friendly**: Seamless experience regardless of query complexity

## 📞 Support

If you encounter any issues:
1. Run the test script to diagnose problems
2. Check API key configuration
3. Review the logs for error messages
4. Ensure all dependencies are installed

Your hybrid chatbot system is now ready to provide intelligent, comprehensive responses to college-related queries! 🎓

