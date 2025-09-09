import re
from typing import Dict, Set

class IntentClassifier:
    """A simple keyword-based intent classifier."""

    def __init__(self):
        self.intent_keywords: Dict[str, Set[str]] = {}
        self.all_keywords: Set[str] = set()
        self.trained = False

    def train(self, training_data: Dict) -> None:
        """Train the classifier with keywords from the training data."""
        for intent, data in training_data.items():
            keywords = set(data.get('keywords', []))
            self.intent_keywords[intent] = keywords
            self.all_keywords.update(keywords)
        self.trained = True

    def classify(self, processed_input: Dict) -> Dict:
        """Classify the intent of the processed input text based on keywords."""
        if not self.trained:
            raise ValueError("Classifier must be trained before classification.")

        clean_tokens = set(processed_input.get('clean_tokens', []))
        
        if not clean_tokens:
            return {'intent': 'unknown', 'confidence': 0.0, 'all_scores': {}}

        intent_scores = {}
        for intent, keywords in self.intent_keywords.items():
            matching_keywords = clean_tokens.intersection(keywords)
            score = len(matching_keywords)
            intent_scores[intent] = score

        # Find the best intent
        if not any(intent_scores.values()):
            best_intent = 'unknown'
            max_score = 0
        else:
            best_intent = max(intent_scores, key=intent_scores.get)
            max_score = intent_scores[best_intent]
        
        total_score = sum(intent_scores.values())
        if total_score == 0:
            confidence = 0.0
        else:
            confidence = max_score / total_score

        if max_score == 1 and total_score == 1:
            confidence = 0.4
        
        if max_score == 0:
            best_intent = 'unknown'
            confidence = 0.0
        
        if confidence < 0.3 and best_intent != 'unknown':
             best_intent = 'unknown'
             confidence = 0.0

        return {
            'intent': best_intent,
            'confidence': confidence,
            'all_scores': intent_scores
        }