from openai import OpenAI
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
try:
    load_dotenv()
except Exception:
    pass

# Read API keys from environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Configure Gemini if key exists
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

def search_college_data(query):
    """
    Searches a predefined dictionary for answers to common questions.
    """
    college_faq = {
        "admission": "Admissions generally open in June. Please check the college website for specific dates.",
        "courses": "We offer B.Tech in Computer Science, Mechanical, and Electronics, as well as MBA and MCA programs.",
        "fees": "The average fee is approximately INR 1,00,000 per year. For a detailed fee structure, please visit the admissions office.",
        "scholarships": "Various merit-based and need-based scholarships are available. You can find details and application forms on the 'Scholarships' section of our website.",
        "hostel": "Yes, hostel facilities are available for both boys and girls with options for AC and non-AC rooms.",
        "placement": "Our college has a dedicated placement cell with a strong track record. Top companies like Microsoft, Google, and Amazon recruit from our campus."
        # Add more keywords and answers
    }
    for keyword in college_faq:
        if keyword in query.lower():
            return college_faq[keyword]
    return None

def fallback_to_llm(query):
    """
    Falls back to a Large Language Model (LLM) if the answer is not in local data.
    Tries Gemini first, then falls back to ChatGPT.
    """
    # Try Gemini first
    try:
        if GOOGLE_API_KEY:
            gemini_model = genai.GenerativeModel("gemini-1.5-flash")
            response = gemini_model.generate_content(query)
            return response.text
    except Exception as e:
        print(f"Gemini API failed with error: {e}")
        # If Gemini fails, try ChatGPT
        try:
            client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API failed with error: {e}")
            return "Sorry, I am having trouble connecting to my knowledge base right now."


def chatbot(query):
    """
    Main chatbot function to process a user query.
    """
    # First, search in the local data
    answer = search_college_data(query)
    if answer:
        return answer
    
    # If not found, use the LLM fallback
    return fallback_to_llm(query)

# Example usage when the script is run directly
if __name__ == "__main__":
    print("Chatbot is ready! Ask a question. Type 'exit' to quit.")
    while True:
        user_query = input("You: ") 
        if user_query.lower() == 'exit':
            break
        response = chatbot(user_query)
        print("Chatbot:", response)