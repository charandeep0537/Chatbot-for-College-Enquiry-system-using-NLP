from typing import Dict, List, Optional
from datetime import datetime, timedelta

class ConversationManager:
    """Manage conversation context and session state."""
    
    def __init__(self):
        self.sessions = {}
        self.context_timeout = timedelta(minutes=30)  # Session timeout
        
    def _cleanup_expired_sessions(self):
        """Remove expired sessions to free memory."""
        current_time = datetime.now()
        expired_sessions = []
        
        for session_id, session_data in self.sessions.items():
            if current_time - session_data['last_activity'] > self.context_timeout:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]
    
    def _get_or_create_session(self, session_id: str) -> Dict:
        """Get existing session or create new one."""
        self._cleanup_expired_sessions()
        
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                'conversation_history': [],
                'user_interests': set(),
                'asked_topics': set(),
                'last_activity': datetime.now(),
                'message_count': 0
            }
        
        return self.sessions[session_id]
    
    def update_context(self, session_id: str, user_message: str, bot_response: str):
        """Update conversation context with new exchange."""
        session = self._get_or_create_session(session_id)
        
        # Add to conversation history
        session['conversation_history'].append({
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': datetime.now()
        })
        
        # Update activity timestamp
        session['last_activity'] = datetime.now()
        session['message_count'] += 1
        
        # Extract and store user interests (simple keyword extraction)
        interests = self._extract_interests(user_message)
        session['user_interests'].update(interests)
        
        # Track asked topics
        topics = self._extract_topics(user_message)
        session['asked_topics'].update(topics)
        
        # Limit history to last 20 exchanges to manage memory
        if len(session['conversation_history']) > 20:
            session['conversation_history'] = session['conversation_history'][-20:]
    
    def _extract_interests(self, message: str) -> set:
        """Extract user interests from message."""
        interests = set()
        message_lower = message.lower()
        
        interest_keywords = {
            'engineering': ['engineering', 'technical', 'programming', 'coding'],
            'business': ['business', 'management', 'mba', 'marketing', 'finance'],
            'science': ['science', 'research', 'laboratory', 'experiment'],
            'arts': ['arts', 'creative', 'design', 'literature'],
            'sports': ['sports', 'athletics', 'gym', 'fitness'],
            'accommodation': ['hostel', 'room', 'accommodation', 'stay']
        }
        
        for interest, keywords in interest_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                interests.add(interest)
        
        return interests
    
    def _extract_topics(self, message: str) -> set:
        """Extract discussed topics from message."""
        topics = set()
        message_lower = message.lower()
        
        topic_keywords = {
            'admission': ['admission', 'apply', 'application'],
            'fees': ['fee', 'cost', 'price', 'tuition'],
            'courses': ['course', 'program', 'subject'],
            'facilities': ['facility', 'lab', 'library'],
            'campus': ['campus', 'location', 'environment'],
            'placement': ['placement', 'job', 'career']
        }
        
        for topic, keywords in topic_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                topics.add(topic)
        
        return topics
    
    def get_context(self, session_id: str) -> Dict:
        """Get current conversation context for a session."""
        session = self._get_or_create_session(session_id)
        return {
            'history_length': len(session['conversation_history']),
            'user_interests': list(session['user_interests']),
            'asked_topics': list(session['asked_topics']),
            'message_count': session['message_count'],
            'session_duration': datetime.now() - session['last_activity']
        }
    
    def get_suggestions(self, session_id: str) -> List[str]:
        """Get contextual suggestions based on conversation history."""
        if session_id not in self.sessions:
            return [
                "Tell me about admissions",
                "What courses do you offer?",
                "What are the campus facilities?",
                "How much are the fees?"
            ]
        
        session = self.sessions[session_id]
        asked_topics = session['asked_topics']
        user_interests = session['user_interests']
        
        # Generate suggestions based on what hasn't been asked yet
        all_topics = {'admission', 'fees', 'courses', 'facilities', 'campus', 'placement', 'faculty'}
        unasked_topics = all_topics - asked_topics
        
        suggestions = []
        
        # Add topic-based suggestions
        topic_suggestions = {
            'admission': "What are the admission requirements?",
            'fees': "Tell me about the fee structure",
            'courses': "What programs do you offer?",
            'facilities': "What facilities are available?",
            'campus': "Tell me about campus life",
            'placement': "How are the placement opportunities?",
            'faculty': "Tell me about the faculty"
        }
        
        for topic in list(unasked_topics)[:3]:
            suggestions.append(topic_suggestions[topic])
        
        # Add interest-based suggestions
        if 'engineering' in user_interests and 'courses' not in asked_topics:
            suggestions.append("What engineering programs do you offer?")
        
        if 'accommodation' in user_interests and 'facilities' not in asked_topics:
            suggestions.append("Tell me about hostel facilities")
        
        # Default suggestions if none generated
        if not suggestions:
            suggestions = [
                "Can you provide contact information?",
                "Tell me about scholarships",
                "What is campus life like?",
                "Do you have sports facilities?"
            ]
        
        return suggestions[:4]  # Limit to 4 suggestions
    
    def reset_context(self, session_id: str):
        """Reset conversation context for a session."""
        if session_id in self.sessions:
            del self.sessions[session_id]
    
    def get_recent_context(self, session_id: str, limit: int = 5) -> List[Dict]:
        """Get recent conversation history."""
        if session_id not in self.sessions:
            return []
        
        history = self.sessions[session_id]['conversation_history']
        return history[-limit:] if history else []