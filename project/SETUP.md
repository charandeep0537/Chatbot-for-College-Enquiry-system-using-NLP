# Chatbot Setup Instructions

## Prerequisites
1. Node.js and npm installed
2. Python 3.8+ installed
3. pip installed

## Installation Steps

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Node.js Dependencies
```bash
npm install
```

### 3. Set up API Keys (Required for AI Fallback)
The chatbot will automatically use both ChatGPT and Gemini AI for questions not in the local knowledge base.

#### Option A: Interactive Setup (Recommended)
```bash
python setup_api_keys.py
```

#### Option B: Manual Setup
Set environment variables:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_openai_api_key_here"
$env:GOOGLE_API_KEY="your_google_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your_openai_api_key_here
set GOOGLE_API_KEY=your_google_api_key_here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
export GOOGLE_API_KEY="your_google_api_key_here"
```

**Note:** The Google API key is already configured in the code, but you can override it with your own key.

## Running the Application

### Option 1: Using npm (Recommended)
```bash
npm run dev --prefix project
```

### Option 2: Manual Start
```bash
# Terminal 1: Start the React frontend
npm run dev

# Terminal 2: Start the Python backend
python app.py
```

## Features

### Local Knowledge Base
The chatbot has a comprehensive local knowledge base covering:
- Admissions information
- Course details
- Fee structure
- Campus facilities
- Faculty information
- Placement details

### AI Integration (ChatGPT + Gemini)
The chatbot automatically uses **both ChatGPT and Gemini AI** for enhanced responses:

1. **Smart AI Fallback**: When confidence < 70% or questions are complex, AI services are used
2. **Dual AI Support**: 
   - **Primary**: Google Gemini AI (gemini-pro model)
   - **Fallback**: OpenAI ChatGPT (gpt-3.5-turbo model)
3. **Context-Aware**: AI responses are tailored for college-related questions
4. **Graceful Degradation**: Falls back to local responses if AI services fail
5. **Real-time Processing**: AI responses are generated in real-time for any question

### Smart Intent Classification
The system uses machine learning to classify user intents and provide contextually appropriate responses.

## API Endpoints

- `POST /api/chat` - Send a message to the chatbot
- `POST /api/reset` - Reset conversation context
- `GET /api/suggestions` - Get conversation suggestions

## Troubleshooting

### Common Issues

1. **AI Services Not Working**
   - Check your internet connection
   - Verify API keys are correctly set
   - Check if you have sufficient API credits

2. **Port Already in Use**
   - The Flask app runs on port 5000
   - The Vite dev server runs on port 5173
   - Make sure these ports are available

3. **Dependencies Issues**
   - Run `pip install -r requirements.txt` again
   - Run `npm install` again

### Getting API Keys

1. **OpenAI API Key:**
   - Visit: https://platform.openai.com/api-keys
   - Create an account and generate an API key

2. **Google API Key:**
   - Visit: https://makersuite.google.com/app/apikey
   - Create an account and generate an API key

## Development

The project structure:
```
project/
├── app.py                 # Flask backend
├── chatbot.py            # Standalone chatbot script
├── chatbot/              # Chatbot modules
│   ├── nlp_processor.py
│   ├── intent_classifier.py
│   ├── response_generator.py
│   ├── conversation_manager.py
│   └── training_data.py
├── src/                  # React frontend
├── dist/                 # Built frontend
└── requirements.txt      # Python dependencies
```
