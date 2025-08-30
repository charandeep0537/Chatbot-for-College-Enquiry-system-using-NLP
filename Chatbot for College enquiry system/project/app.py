from flask import Flask, request, jsonify, session, send_from_directory
import secrets
import logging
import os
from datetime import datetime
from chatbot.nlp_processor import NLPProcessor
from chatbot.intent_classifier import IntentClassifier
from chatbot.response_generator import ResponseGenerator
from chatbot.conversation_manager import ConversationManager
from chatbot.training_data import TRAINING_DATA

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='dist', static_url_path='')
app.secret_key = secrets.token_hex(16)

# Initialize chatbot components
nlp_processor = NLPProcessor()
intent_classifier = IntentClassifier()
response_generator = ResponseGenerator()
conversation_manager = ConversationManager()

# Train the intent classifier with sample data
intent_classifier.train(TRAINING_DATA)

@app.route('/')
def index():
    """Serve the React frontend."""
    if 'session_id' not in session:
        session['session_id'] = secrets.token_hex(8)
    return send_from_directory('dist', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages and return chatbot responses."""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        session_id = session.get('session_id')
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Process the user message
        processed_input = nlp_processor.process(user_message)
        
        # Classify intent
        intent_result = intent_classifier.classify(processed_input)
        
        # Generate response
        response_data = response_generator.generate_response(
            intent_result, processed_input, session_id
        )
        
        # Update conversation context
        conversation_manager.update_context(
            session_id, user_message, response_data['response']
        )
        
        # Log the interaction
        logger.info(f"Session {session_id}: Intent={intent_result['intent']}, "
                   f"Confidence={intent_result['confidence']:.2f}")
        
        return jsonify({
            'response': response_data['response'],
            'intent': intent_result['intent'],
            'confidence': intent_result['confidence'],
            'suggestions': response_data.get('suggestions', []),
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error processing chat message: {str(e)}")
        return jsonify({
            'response': "I'm sorry, I encountered an error. Please try again.",
            'error': True
        }), 500

@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    """Reset the conversation context."""
    session_id = session.get('session_id')
    if session_id:
        conversation_manager.reset_context(session_id)
    return jsonify({'status': 'success'})

@app.route('/api/suggestions')
def get_suggestions():
    """Get conversation suggestions based on current context."""
    session_id = session.get('session_id')
    suggestions = conversation_manager.get_suggestions(session_id)
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)