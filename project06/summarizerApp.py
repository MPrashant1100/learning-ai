# summarizerApp.py
# CLI Summarizer App

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the Gemini API key
load_dotenv(dotenv_path=".env.local")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Get user input
print("📝 Paste the text you want to summarize:")
user_input = input("\nYour text: ")

# Prompt with role + task + constraint
prompt = f"""
You are a summarizer bot.
Summarize the following content in 4 bullet points:
{user_input}
"""

# Call Gemini to generate summary
response = model.generate_content(prompt)

# Show output .
print("\n📌 Summary:")
print(response.text)
