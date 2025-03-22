#Stores API Configuration
import google.generativeai as genai

# Configure Gemini with your API key
GEMINI_API_KEY = "Your api key"
genai.configure(api_key=GEMINI_API_KEY)

# Use the correct model name
model = genai.GenerativeModel('gemini-1.5-pro-latest')
