# day11.py
# This script covers F-strings, docstrings, PEP 8 guidelines, and the Zen of Python.

# ==========================
# Part 1: F-strings
# ==========================
# F-strings provide a way to embed expressions inside string literals, using curly braces {}.

# Using the format() method
letter = "Hey, my name is {} and I am from {}"
country = "Bangladesh"
name = "Khalid"
print(letter.format(name, country))

# Using F-strings
print(f"Hey, my name is {name} and I am from {country}")

# Formatting numbers with F-strings
price = 49.95000005
print(f"For only {price:.2f} dollars!")

# ==========================
# Part 2: Docstrings
# ==========================
# Docstrings provide a convenient way of associating documentation with Python modules, functions, classes, and methods.

def square(n):
    '''This function returns the square of the number.'''
    return n ** 2

# Accessing the docstring
print(square.__doc__)

# ==========================
# Part 3: PEP 8 Guidelines
# ==========================
# PEP 8 is the style guide for Python code. Here are some key points:
# 1. Indentation: Use 4 spaces per indentation level.
# 2. Line length: Limit all lines to a maximum of 79 characters.
# 3. Blank lines: Use blank lines to separate functions and classes, and larger blocks of code inside functions.
# 4. Comments: Use comments to explain code. Inline comments should be separated by at least two spaces from the statement.
# 5. Naming conventions: Use descriptive names for variables, functions, classes, and modules.

# Example of proper indentation
def example_function():
    x = 1
    y = 2
    if x < y:
        print("x is less than y")

# Example of comments
x = 5  # This is an inline comment
# This is a block comment explaining the following block of code
y = 10
z = x + y
print(z)

# Example of naming conventions
my_variable = 42
def my_function():
    pass

# ==========================
# Part 4: Zen of Python
# ==========================
# The Zen of Python is a collection of 19 guiding principles for writing computer programs in Python.

import this

# The Zen of Python will be printed when the module is imported
# It includes principles like "Simple is better than complex" and "Readability counts."

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. F-strings for string formatting.
# 2. Docstrings for documentation.
# 3. PEP 8 guidelines for writing clean and readable Python code.
# 4. The Zen of Python, which provides guiding principles for writing Pythonic code.

# End of day 11 learning
