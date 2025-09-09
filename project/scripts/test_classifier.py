from chatbot.nlp_processor import NLPProcessor
from chatbot.intent_classifier import IntentClassifier
from chatbot.response_generator import ResponseGenerator
from chatbot.training_data import TRAINING_DATA

TEST_QUERIES = [
    "hi there",
    "how to apply for admission?",
    "what are the fees for computer science?",
    "what courses do you offer in engineering?",
    "tell me about hostel and sports facilities",
    "where is the campus located?",
    "tell me about your professors",
    "how is the placement record and average salary?",
    "are scholarships available and how to apply?",
    "what documents are required for application?",
    "when is the application deadline?",
    "is there any entrance exam?",
    "asdf qwer zxcv",
]

def main():
    nlp = NLPProcessor()
    clf = IntentClassifier()
    resp = ResponseGenerator()

    clf.train(TRAINING_DATA)

    for q in TEST_QUERIES:
        processed = nlp.process(q)
        result = clf.classify(processed)
        response = resp.generate_response(result, processed, session_id="test")
        print("--")
        print(f"Q: {q}")
        print(f"Intent: {result['intent']}  Confidence: {result['confidence']:.2f}")
        print(f"Resp: {response['response']}")
        if response.get('suggestions'):
            print(f"Suggs: {response['suggestions']}")

if __name__ == "__main__":
    main()


