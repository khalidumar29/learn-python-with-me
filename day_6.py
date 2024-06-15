# This script covers the time module, conditional statements for greetings, match statement, and different types of loops in Python.

import time

# ==========================
# Part 1: Using the time module
# ==========================
# The time module provides various time-related functions.

# Get the current time as a string in the format HH:MM:SS
timestamp = time.strftime("%H:%M:%S")
print("Current Time:", timestamp)

# ==========================
# Part 2: Conditional Greetings Based on the Hour
# ==========================
# Get the current hour
hour = int(time.strftime("%H"))

# Print a greeting based on the current hour
if hour < 12:
    print("Good Morning")
elif hour < 16:
    print("Good Afternoon")
elif hour < 20:
    print("Good Evening")
else:
    print("Good Night")

# ==========================
# Part 3: match Statement
# ==========================
# The match statement is used for pattern matching. It is similar to switch-case in other languages.

x = 10
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if x > 10:
        print("x is greater than 10")
    case _:
        print("x is", x)

# ==========================
# Part 4: Loops in Python
# ==========================
# Loops are used to iterate over a sequence of elements.

# For loop to iterate over characters in a string
name = "khalid umar"
print("For loop over a string:")
for i in name:
    print(i)

# For loop with range to generate a sequence of numbers
print("For loop with range:")
for k in range(1, 11, 2):  # start, stop, step
    print(k)

# While loop to repeat a block of code as long as a condition is true
print("While loop:")
i = 0
while i < 3:
    print(i)
    i += 1
print("Done with the while loop")

# Do-while loop emulation using a while loop
print("Do-while loop emulation:")
i = 0
while True:
    print(i)
    i += 1
    if i >= 3:
        break
print("Done with the do-while loop")

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Using the time module to get the current time.
# 2. Conditional statements to print greetings based on the current hour.
# 3. The match statement for pattern matching.
# 4. Different types of loops: for loop, while loop, and do-while loop emulation.

# End of day 6 learning