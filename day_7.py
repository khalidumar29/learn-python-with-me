# This script covers break and continue statements and function definitions in Python.

# ==========================
# Part 1: break and continue Statements
# ==========================
# The break statement is used to exit a loop prematurely.
# The continue statement is used to skip the rest of the code inside the loop for the current iteration.

# Example of using break statement in a for loop
for i in range(12):
    print("5 X", i + 1, "=", 5 * (i + 1))
    if i == 10:
        break

print("Loop is broken after reaching the condition.")

# Example of using continue statement in a for loop
for i in range(12):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print("This is an odd number:", i)

# ==========================
# Part 2: Functions
# ==========================
# Functions are blocks of code that perform a specific task. They can take inputs (arguments) and return outputs.

# Define a function to calculate the geometric mean of two numbers
def gmeanCalculate(a, b):
    mean = (a * b) / (a + b)
    print("Geometric mean of", a, "and", b, "is:", mean)

# Define a function to determine the greater number between two numbers
def greaterNum(a, b):
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")

# Call the functions with example arguments
gmeanCalculate(5, 2)
greaterNum(10, 25)

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. The break statement to exit loops prematurely.
# 2. The continue statement to skip the rest of the code inside the loop for the current iteration.
# 3. Defining and using functions to encapsulate code for specific tasks.

# End of day 7 learning
