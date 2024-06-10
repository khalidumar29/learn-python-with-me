# This script covers variables, data types, operators, typecasting, and taking input from the user.
# It also includes a simple calculator exercise.

# ==========================
# Part 1: Variables
# ==========================
# Variables are used to store data in Python. You can create a variable by simply assigning a value to a name.

# Example of creating variables
a = 10
b = 5.5
name = "Python"

# ==========================
# Part 2: Data Types
# ==========================
# In Python, every piece of data is an object. Some basic data types include:
# int, float, str, list, tuple, dict, and bool.

# Example of different data types
integer_variable = 42
float_variable = 3.14
string_variable = "Hello, Python!"
list_variable = [1, 2, 3, 4, 5]
tuple_variable = (1, 2, 3)
dict_variable = {"key": "value"}
bool_variable = True

# Print the type of each variable
print("Type of integer_variable:", type(integer_variable))
print("Type of float_variable:", type(float_variable))
print("Type of string_variable:", type(string_variable))
print("Type of list_variable:", type(list_variable))
print("Type of tuple_variable:", type(tuple_variable))
print("Type of dict_variable:", type(dict_variable))
print("Type of bool_variable:", type(bool_variable))

# ==========================
# Part 3: Operators
# ==========================
# Operators are used to perform operations on variables and values. Some basic operators include:
# Arithmetic Operators: +, -, *, /, %, **, //
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not

# Example of arithmetic operators
x = 10
y = 3
print("x + y =", x + y)  # Addition
print("x - y =", x - y)  # Subtraction
print("x * y =", x * y)  # Multiplication
print("x / y =", x / y)  # Division
print("x % y =", x % y)  # Modulus
print("x ** y =", x ** y)  # Exponentiation
print("x // y =", x // y)  # Floor Division

# ==========================
# Part 4: Taking Input from User
# ==========================
# You can take input from the user using the input() function. The input() function returns the input as a string.

# Example of taking input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# ==========================
# Part 5: Typecasting
# ==========================
# Typecasting is the process of converting one data type to another.

# Example of typecasting
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print("Type of num_str:", type(num_str))
print("Type of num_int:", type(num_int))

# ==========================
# Exercise 1: Simple Calculator
# ==========================
# Create a simple calculator that takes two numbers and an operator from the user,
# performs the calculation, and prints the result.

# Taking inputs from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")

# Convert inputs to appropriate data types
num1 = float(num1)
num2 = float(num2)

# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
print("The result is:", result)

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Variables and their usage.
# 2. Basic data types in Python.
# 3. Operators for performing various operations.
# 4. Taking input from the user.
# 5. Typecasting to convert data types.
# 6. A simple calculator exercise to apply the concepts learned.

# End of day 2 learning

# Author: Khalid Umar
# Contact: khalid100umar@gmail.com
# Portfolio: https://khalid-umar.com
