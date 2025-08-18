# import tiktoken

# # Use GPT-3.5 tokenizer
# encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# prompt = "Summarize the Bhagavad Gita in 3 bullet points."
# tokens = encoding.encode(prompt)

# print("Tokens:", tokens)
# print("Token count:", len(tokens))

# chatgpt_cli.py

# chatgpt_cli.py

from openai import OpenAI

# Create client with your API key
client = OpenAI(api_key="key")

# Loop for continuous chatting
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended. Goodbye! 👋")
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or gpt-4 if you have access
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content
    print("AI:", reply)

