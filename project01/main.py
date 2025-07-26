print("Welcome to the AI Motivation App 🔥\n")

name = input ("Enter the name ")
age = int(input("Enter the age "))
goal = input("What’s your goal in AI? ")

goal = goal.strip().lower()

print("Your Personal Motivation Message:")
print(f"Hey {name} ({age}), your goal to \"{goal}\" is powerful.")