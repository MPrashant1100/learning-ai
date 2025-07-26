# Prompt Cleaner + File Writer
# day3_prompt_cleaner.py

import re

def clean_text(text) :
    text = text.strip().lower()              # Remove leading/trailing spaces, lowercase
    text = re.sub(r'[^\w\s]','', text)       # Remove punctuation using regex

    return text

print("🧼 Welcome to the Prompt Cleaner & Saver!\n")

prompts = []

for i in range(3):
    raw_prompt = input(f"Enter prompt {i+1}: ")
    prompts.append(raw_prompt)

with open("cleaned_prompts.txt", "w") as file:
    file.write("Original Prompt → Cleaned Prompt\n")
    file.write("----------------------------------\n")
    for prompt in prompts:
        cleaned = clean_text(prompt)
        file.write(f"{prompt} → {cleaned}\n")

print("\n✅ All prompts cleaned and saved to 'cleaned_prompts.txt'")