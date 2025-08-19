# gemini_agent.py

import google.generativeai as genai

# Replace with your actual key
genai.configure(api_key="Your_API_KEY")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

print("🤖 Gemini AI Agent Activated! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye 👋")
        break

    try:
        response = model.generate_content(user_input)
        print(f"Agent: {response.text}\n")
    except Exception as e:
        print(f"❌ Error: {e}")
