# gemini_agent.py

import google.generativeai as genai

# Replace with your actual key
genai.configure(api_key="Your_API_KEY")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

print("🤖 Gemini AI Agent Activated! Type 'exit' to quit.\n")

conversation = []  # stores memory

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye 👋")
        break

    conversation.append({"role": "user", "parts": [user_input]})

    try:
        # response = model.generate_content(user_input)
        # print(f"Agent: {response.text}\n")
         # Ask the model with full conversation history
        response = model.generate_content(conversation)
        print("Agent:", response.text)

        # Add assistant response to memory
        conversation.append({"role": "model", "parts": [response.text]})
    except Exception as e:
        print(f"❌ Error: {e}")
