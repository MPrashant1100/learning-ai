# Prompt Logger & Word Analyzer

print("Welcome to the Prompt Logger ✍️\n")

prompts = []

for i in range(3):
    prompt = input (f"Enter prompt {i+1}: ")
    prompts.append(prompt)

print("\n✅ Here are your prompts: ")

for prompt in prompts:
    print(f"prompt: ", prompt )