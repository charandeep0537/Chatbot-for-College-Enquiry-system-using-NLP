import re
import string
from typing import Dict, List, Set

class NLPProcessor:
    """Natural Language Processing component for text preprocessing and analysis."""
    
    def __init__(self):
        self.stop_words = {
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
            'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 
            'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 
            'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
            'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 
            'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
            'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
            'with', 'through', 'during', 'before', 'after', 'above', 'below', 
            'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 
            'further', 'then', 'once'
        }
        
        # Simple lemmatization map for common plural/synonym forms
        self.lemma_map = {
            'admissions': 'admission',
            'requirements': 'requirement',
            'exams': 'exam',
            'fees': 'fee',
            'payments': 'payment',
            'courses': 'course',
            'programs': 'program',
            'subjects': 'subject',
            'facilities': 'facility',
            'libraries': 'library',
            'labs': 'lab',
            'hostels': 'hostel',
            'campuses': 'campus',
            'teachers': 'teacher',
            'professors': 'professor',
            'companies': 'company',
            'salaries': 'salary',
            'placements': 'placement',
            'scholarships': 'scholarship'
        }

        # College-specific keywords and their categories
        self.keyword_categories = {
            'admission': ['admission', 'apply', 'application', 'eligibility', 'requirement', 
                         'qualify', 'entrance', 'cutoff', 'merit', 'selection'],
            'fees': ['fee', 'cost', 'price', 'tuition', 'scholarship', 'financial', 
                    'payment', 'expense', 'money', 'affordable'],
            'scholarship': ['scholarship', 'grant', 'aid', 'financial', 'merit', 'need'],
            'courses': ['course', 'program', 'degree', 'subject', 'major', 'minor', 
                       'curriculum', 'syllabus', 'credit', 'semester'],
            'facilities': ['facility', 'library', 'lab', 'hostel', 'accommodation', 'dorm', 'room', 'mess', 'security', 'cafeteria', 
                          'gym', 'sports', 'wifi', 'transport', 'infrastructure'],
            'campus': ['campus', 'location', 'area', 'size', 'building', 'environment', 
                      'atmosphere', 'life', 'culture', 'events'],
            'faculty': ['faculty', 'teacher', 'professor', 'staff', 'instructor', 
                       'mentor', 'guidance', 'experience', 'qualification'],
            'placement': ['placement', 'job', 'career', 'company', 'salary', 
                         'internship', 'recruitment', 'opportunity', 'employment'],
            'documents': ['document', 'certificate', 'transcript', 'marksheet', 'id', 'photo', 'proof'],
            'deadline': ['deadline', 'date', 'closing', 'last'],
            'entrance': ['entrance', 'exam', 'test', 'cutoff', 'eamcet', 'ecet']
        }
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenize text into individual words."""
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)
        
        # Split into tokens and remove empty strings
        tokens = [token.strip() for token in text.split() if token.strip()]
        return tokens
    
    def lemmatize_tokens(self, tokens: List[str]) -> List[str]:
        """Apply simple lemma mapping to tokens."""
        return [self.lemma_map.get(token, token) for token in tokens]

    def remove_stop_words(self, tokens: List[str]) -> List[str]:
        """Remove common stop words from tokens."""
        return [token for token in tokens if token not in self.stop_words]
    
    def extract_keywords(self, tokens: List[str]) -> Dict[str, List[str]]:
        """Extract and categorize keywords from tokens."""
        categorized_keywords = {}
        
        for category, keywords in self.keyword_categories.items():
            found_keywords = [token for token in tokens if token in keywords]
            if found_keywords:
                categorized_keywords[category] = found_keywords
        
        return categorized_keywords
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract named entities like numbers, emails, etc."""
        entities = {
            'numbers': re.findall(r'\b\d+\b', text),
            'emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text),
            'years': re.findall(r'\b(19|20)\d{2}\b', text),
            'percentages': re.findall(r'\b\d+(\.\d+)?%\b', text)
        }
        
        # Remove empty lists
        return {k: v for k, v in entities.items() if v}
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate simple similarity between two texts based on common words."""
        tokens1 = set(self.remove_stop_words(self.tokenize(text1)))
        tokens2 = set(self.remove_stop_words(self.tokenize(text2)))
        
        if not tokens1 or not tokens2:
            return 0.0
        
        intersection = tokens1.intersection(tokens2)
        union = tokens1.union(tokens2)
        
        return len(intersection) / len(union)
    
    def process(self, text: str) -> Dict:
        """Main processing function that returns comprehensive text analysis."""
        tokens = self.tokenize(text)
        tokens = self.lemmatize_tokens(tokens)
        clean_tokens = self.remove_stop_words(tokens)
        keywords = self.extract_keywords(clean_tokens)
        entities = self.extract_entities(text)
        
        return {
            'original_text': text,
            'tokens': tokens,
            'clean_tokens': clean_tokens,
            'keywords': keywords,
            'entities': entities,
            'word_count': len(tokens),
            'clean_word_count': len(clean_tokens)
        }