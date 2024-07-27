# day10.py
# This script creates a program that simulates a simple version of "Kaun Banega Crorepati" (KBC) using lists.

# ==========================
# KBC Game Simulation
# ==========================
print("Welcome to KBC")

# List of questions, options, and correct answers
questions = [
    "What is the capital of Bangladesh?",
    "Who is the PM of Bangladesh?",
    "What is the currency of Bangladesh?"
]
options = [
    ["Dhaka", "Chittagong", "Rajshahi", "Khulna"],
    ["Sheikh Hasina", "Khaleda Zia", "Ershad", "Mujib"],
    ["Taka", "Dollar", "Euro", "Pound"]
]
answers = ["Dhaka", "Sheikh Hasina", "Taka"]

# Initial amount won by the user
amount = 1000000

# Loop through the questions
for i in range(len(questions)):
    print(f"\nQuestion {i + 1}: {questions[i]}")
    for j in range(4):
        print(f"{j + 1}. {options[i][j]}")

    # Take user input for answer
    user_input = int(input("Enter your answer (1-4): "))

    # Check if the user's answer is correct
    if options[i][user_input - 1] == answers[i]:
        print("Correct Answer!")
        print(f"You have won {amount}!")
        amount *= 10  # Increase the amount for the next question
    else:
        print("Wrong Answer!")
        break  # Exit the loop if the answer is wrong

# Display final amount won by the user
print(f"\nYou have won a total of {amount // 10}!")
print("Thank you for playing KBC.")

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Creating a list of questions, options, and correct answers.
# 2. Displaying questions and options to the user.
# 3. Taking user input and checking if the answer is correct.
# 4. Calculating and displaying the final amount won by the user.

# End of day 10 learning
