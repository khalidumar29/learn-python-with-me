# This script covers function arguments (multiple arguments, default arguments, ordered arguments, and
# required arguments) and an introduction to lists.

# ==========================
# Part 1: Function Arguments
# ==========================
# Functions can have different types of arguments including default, multiple, ordered, and required arguments.

# Default arguments
def average(a=5, b=6):
    print("The average is", (a + b) / 2)


# Calling the function with and without arguments
average(5, 2)
average(b=5, a=10)
average()  # Uses default values


# Multiple arguments using *args
def new_average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average is:", sum / len(numbers))


# Calling the function with a varying number of arguments
new_average(5, 6, 7, 8)

# ==========================
# Part 2: Introduction to Lists
# ==========================
# Lists are ordered collections of items which can be of different types.

# Example list
l = [3, 5, 6]

# Checking for an item in the list
if 7 in l:
    print("Yes, 7 is in the list")
else:
    print("No, 7 is not in the list")

# List comprehension with condition
list_comp = [i * i for i in range(10) if i % 2 == 0]
print("List comprehension result:", list_comp)

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Function arguments including default arguments and multiple arguments using *args.
# 2. Ordered and required arguments.
# 3. Introduction to lists, including list operations and list comprehensions.

# End of day 8 learning
