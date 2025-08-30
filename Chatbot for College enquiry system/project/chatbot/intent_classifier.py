import re
from typing import Dict, List, Tuple
from collections import defaultdict

class IntentClassifier:
    """Intent classification component using pattern matching and keyword analysis."""
    
    def __init__(self):
        self.intent_patterns = {}
        self.keyword_weights = {}
        self.trained = False
    
    def train(self, training_data: Dict) -> None:
        """Train the classifier with intent patterns and examples."""
        for intent, data in training_data.items():
            patterns = []
            keywords = defaultdict(int)
            training_keywords = set(data.get('keywords', []))
            
            # Extract patterns from examples
            for example in data.get('examples', []):
                # Create regex patterns from examples
                pattern = self._create_pattern(example)
                patterns.append(pattern)
                
                # Count keywords for weight calculation
                words = example.lower().split()
                for word in words:
                    keywords[word] += 1
            
            # Store patterns and calculate keyword weights
            self.intent_patterns[intent] = patterns
            # Include provided training keywords with a base weight boost
            for kw in training_keywords:
                keywords[kw] += 2
            self.keyword_weights[intent] = dict(keywords)
        
        self.trained = True
    
    def _create_pattern(self, example: str) -> str:
        """Create a regex pattern from an example sentence."""
        # Replace specific words with more general patterns
        pattern = example.lower()
        
        # Replace numbers with number pattern
        pattern = re.sub(r'\b\d+\b', r'\\d+', pattern)
        
        # Replace optional words with optional groups
        pattern = re.sub(r'\b(can|could|would|will|please|kindly)\b', r'(?:\\w+\\s+)?', pattern)
        
        # Make pattern more flexible
        pattern = pattern.replace(' ', r'\s+')
        pattern = f'.*{pattern}.*'
        
        return pattern
    
    def _calculate_pattern_score(self, processed_input: Dict, intent: str) -> float:
        """Calculate pattern matching score for an intent."""
        text = processed_input['original_text'].lower()
        patterns = self.intent_patterns.get(intent, [])
        
        max_score = 0.0
        for pattern in patterns:
            try:
                if re.search(pattern, text):
                    # Calculate match quality based on pattern complexity
                    pattern_score = min(1.0, len(pattern) / (len(text) + 1))
                    max_score = max(max_score, pattern_score)
            except re.error:
                continue
        
        return max_score
    
    def _calculate_keyword_score(self, processed_input: Dict, intent: str) -> float:
        """Calculate keyword matching score for an intent."""
        clean_tokens = processed_input['clean_tokens']
        intent_keywords = self.keyword_weights.get(intent, {})
        
        if not intent_keywords or not clean_tokens:
            return 0.0
        
        score = 0.0
        total_weight = sum(intent_keywords.values())
        
        for token in clean_tokens:
            if token in intent_keywords:
                weight = intent_keywords[token] / total_weight
                score += weight
        
        return min(1.0, score)
    
    def _calculate_category_score(self, processed_input: Dict, intent: str) -> float:
        """Calculate score based on keyword categories."""
        keywords = processed_input.get('keywords', {})
        
        # Intent to category mapping
        intent_categories = {
            'greeting': [],
            'admission_info': ['admission'],
            'fee_info': ['fees'],
            'course_info': ['courses'],
            'facility_info': ['facilities'],
            'campus_info': ['campus'],
            'faculty_info': ['faculty'],
            'placement_info': ['placement'],
            'scholarship_info': ['scholarship', 'fees'],
            'hostel_info': ['facilities'],
            'documents_required': ['documents', 'admission'],
            'application_deadline': ['deadline', 'admission'],
            'entrance_exam_info': ['entrance', 'admission'],
            'contact_info': [],
            'goodbye': []
        }
        
        relevant_categories = intent_categories.get(intent, [])
        if not relevant_categories:
            return 0.0
        
        score = 0.0
        for category in relevant_categories:
            if category in keywords:
                score += 1.0 / len(relevant_categories)
        
        return score
    
    def classify(self, processed_input: Dict) -> Dict:
        """Classify the intent of processed input text."""
        if not self.trained:
            raise ValueError("Classifier must be trained before classification")
        
        intent_scores = {}
        
        for intent in self.intent_patterns.keys():
            # Combine different scoring methods
            pattern_score = self._calculate_pattern_score(processed_input, intent)
            keyword_score = self._calculate_keyword_score(processed_input, intent)
            category_score = self._calculate_category_score(processed_input, intent)
            
            # Weighted combination of scores
            combined_score = (
                pattern_score * 0.35 + 
                keyword_score * 0.45 + 
                category_score * 0.20
            )
            
            intent_scores[intent] = combined_score
        
        # Find best matching intent
        best_intent = max(intent_scores, key=intent_scores.get)
        confidence = intent_scores[best_intent]
        
        # Apply confidence threshold with category-based fallback
        if confidence < 0.3:
            # Try to infer category directly and map to a broad intent
            keywords = processed_input.get('keywords', {})
            category_to_intent = {
                'admission': 'admission_info',
                'fees': 'fee_info',
                'courses': 'course_info',
                'facilities': 'facility_info',
                'scholarship': 'scholarship_info',
                'documents': 'documents_required',
                'deadline': 'application_deadline',
                'entrance': 'entrance_exam_info',
                'campus': 'campus_info',
                'faculty': 'faculty_info',
                'placement': 'placement_info'
            }
            for category, mapped_intent in category_to_intent.items():
                if category in keywords:
                    best_intent = mapped_intent
                    confidence = 0.35
                    break
            else:
                best_intent = 'unknown'
                confidence = 0.0
        
        return {
            'intent': best_intent,
            'confidence': confidence,
            'all_scores': intent_scores
        }