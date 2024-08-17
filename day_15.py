# Finally Keyword in Exception Handling

# Example of using the 'finally' keyword
try:
    print(1 / 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(e)  # Handling the division by zero error
finally:
    # The finally block executes no matter what, whether there is an exception or not
    print("This is finally block and it will always execute no matter what")

# Raising Exceptions
# Asking the user for a number and raising an error if it's not in the specified range
a = int(input("Enter a number between 1 and 5: "))

# Using 'raise' to manually trigger a ValueError if the input is not in the range 1 to 5
if not 1 <= a <= 5:
    raise ValueError("The value is not in the range of 1 to 5")

# Quiz Game Implementation

# List of questions and their corresponding answers
questions = [
    ["Which language was used to create Facebook?", "Python", "French", "Java", "C++", "1"],
    ["Which of the following is not a programming language?", "Python", "C++", "Java", "French", "4"],
    ["Which of the following is not a programming language?", "Python", "C++", "Java", "French", "4"]
]

# List of levels corresponding to the prize money
level = [1000, 2000, 3000, 4000, 5000]

# Loop through each question in the quiz
for i in range(len(questions)):
    current_question = questions[i]

    # Display the current question and the prize for answering it correctly
    print(f"Question for Rs {level[i]}")
    print(f"a. {current_question[1]}")
    print(f"b. {current_question[2]}")
    print(f"c. {current_question[3]}")
    print(f"d. {current_question[4]}")

    # Get the user's reply
    reply = input("Enter your answer: ")

    # Check if the reply is correct
    if reply == current_question[5]:
        print("Correct answer")
    else:
        print("Wrong answer")
        break  # Exit the loop if the answer is wrong
