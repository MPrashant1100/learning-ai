# Day 7: Text Summarization using LLMs
# #	Topic
# 1️⃣	What is Text Summarization? Types (Extractive vs Abstractive)
# 2️⃣	Prompt Patterns for Summarization (Role, Format, Constraints)
# 3️⃣	Build: Summarize a Blog Post using Gemini or OpenAI
# 4️⃣	Bonus: Chunking Large Texts with Python 

# 🧰 The 3-Part Prompt Framework

# Always structure your summarization prompt like this:

# ==>> [ROLE] + [TASK] + [CONSTRAINTS]

# 🔍 Let’s Break It Down
# 1️⃣ [ROLE] → Who is the model pretending to be?

# Helps bring tone, perspective, and depth

# Role	Output Style
# News Editor	Factual, professional
# Teacher	Simple, clear explanation
# Spiritual Guide	Thoughtful, moral insights
# Product Manager	Bullet points, focus on action

# 🔹 Example:

# “You are a spiritual teacher. Summarize the following text into 2 key life lessons.”

# 2️⃣ [TASK] → What do you want?

# Be very clear!

# Task	Example
# Summarize	“Summarize this in 3 bullet points.”
# Explain	“Explain this like I’m a 10-year-old.”
# TL;DR	“Give me a 1-line TL;DR.”
# Compare	“Compare the two sections in summary.”
# 3️⃣ [CONSTRAINTS] → Set rules

# This makes results repeatable and focused.

# Constraint	Effect
# Word limit	Makes output concise
# Language	You can say: “in Hindi”
# Format	Like: “in JSON or Markdown”

# 🧠 Example:

# “Summarize this Gita verse in simple Hindi, max 3 lines.”
