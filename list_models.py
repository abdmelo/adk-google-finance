import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load from specific subdirectory
load_dotenv("credit_score_adk/.env")
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API Key not found in credit_score_adk/.env")
else:
    genai.configure(api_key=api_key)
    try:
        print("Listing available models:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
    except Exception as e:
        print(f"Error: {e}")
