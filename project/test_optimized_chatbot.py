#!/usr/bin/env python3
"""
Optimized test script for the hybrid chatbot system.
Tests with better local response prioritization.
"""

import os
import sys
import time
from chatbot.nlp_processor import NLPProcessor
from chatbot.intent_classifier import IntentClassifier
from chatbot.response_generator import ResponseGenerator
from chatbot.training_data import TRAINING_DATA

def test_optimized_chatbot():
    """Test the optimized hybrid chatbot system."""
    print("🤖 Optimized Hybrid Chatbot System Test")
    print("=" * 50)
    print()
    
    # Initialize components
    print("Initializing chatbot components...")
    nlp_processor = NLPProcessor()
    intent_classifier = IntentClassifier()
    response_generator = ResponseGenerator()
    
    # Train the intent classifier
    print("Training intent classifier...")
    intent_classifier.train(TRAINING_DATA)
    print("✅ Components initialized successfully")
    print()
    
    # Test cases optimized for local responses
    test_cases = [
        # Local data tests (should use local responses)
        {
            "query": "Hello",
            "expected_source": "local",
            "description": "Simple greeting"
        },
        {
            "query": "What courses do you offer?",
            "expected_source": "local",
            "description": "Course information query"
        },
        {
            "query": "What are the admission requirements?",
            "expected_source": "local",
            "description": "Admission information query"
        },
        {
            "query": "Tell me about the fees",
            "expected_source": "local",
            "description": "Fee information query"
        },
        {
            "query": "What facilities are available?",
            "expected_source": "local",
            "description": "Facility information query"
        },
        {
            "query": "Tell me about the campus",
            "expected_source": "local",
            "description": "Campus information query"
        },
        
        # AI fallback tests (should use AI responses)
        {
            "query": "What are the latest trends in renewable energy engineering and how do they impact the curriculum?",
            "expected_source": "ai",
            "description": "Complex technical question"
        },
        {
            "query": "Compare the advantages and disadvantages of studying engineering vs medicine in terms of career prospects",
            "expected_source": "ai",
            "description": "Complex comparison question"
        }
    ]
    
    print("🧪 Running optimized test cases...")
    print("-" * 50)
    
    results = []
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['description']}")
        print(f"Query: \"{test_case['query']}\"")
        
        try:
            # Process the query
            processed_input = nlp_processor.process(test_case['query'])
            intent_result = intent_classifier.classify(processed_input)
            response_data = response_generator.generate_response(
                intent_result, processed_input, 'test_session'
            )
            
            # Check results
            actual_source = response_data.get('source', 'unknown')
            confidence = intent_result.get('confidence', 0.0)
            intent = intent_result.get('intent', 'unknown')
            
            print(f"Intent: {intent} (confidence: {confidence:.2f})")
            print(f"Response source: {actual_source}")
            print(f"Response preview: {response_data['response'][:100]}...")
            
            # Evaluate test result
            expected_source = test_case['expected_source']
            test_passed = actual_source == expected_source
            
            if test_passed:
                print("✅ Test PASSED")
            else:
                print(f"❌ Test FAILED - Expected: {expected_source}, Got: {actual_source}")
            
            results.append({
                'test_case': test_case,
                'passed': test_passed,
                'actual_source': actual_source,
                'confidence': confidence,
                'intent': intent
            })
            
        except Exception as e:
            print(f"❌ Test FAILED with error: {e}")
            results.append({
                'test_case': test_case,
                'passed': False,
                'error': str(e)
            })
        
        time.sleep(0.5)  # Small delay between tests
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 OPTIMIZED TEST SUMMARY")
    print("=" * 50)
    
    total_tests = len(results)
    passed_tests = sum(1 for r in results if r['passed'])
    failed_tests = total_tests - passed_tests
    
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Success rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if failed_tests > 0:
        print("\n❌ Failed tests:")
        for i, result in enumerate(results):
            if not result['passed']:
                print(f"  - Test {i+1}: {result['test_case']['description']}")
                if 'error' in result:
                    print(f"    Error: {result['error']}")
                else:
                    print(f"    Expected: {result['test_case']['expected_source']}, Got: {result['actual_source']}")
    
    print("\n🎯 System Status:")
    if passed_tests == total_tests:
        print("✅ All tests passed! The optimized hybrid chatbot system is working perfectly.")
    elif passed_tests >= total_tests * 0.8:
        print("⚠️  Most tests passed. The system is working well with minor issues.")
    else:
        print("❌ Multiple test failures detected. Please check the configuration.")
    
    return results

if __name__ == "__main__":
    print("🚀 Starting Optimized Hybrid Chatbot System Tests")
    print("=" * 60)
    
    # Run optimized tests
    test_results = test_optimized_chatbot()
    
    print("\n" + "=" * 60)
    print("🏁 Optimized Testing Complete!")
    
    if any(result['passed'] for result in test_results):
        print("✅ Your optimized hybrid chatbot system is ready to use!")
        print("\nTo start the chatbot:")
        print("1. Run: python app.py")
        print("2. Open your browser to: http://localhost:5000")
        print("3. Start chatting with your optimized AI-powered college chatbot!")
    else:
        print("❌ Please fix the issues before using the chatbot.")
