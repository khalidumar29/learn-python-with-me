# This script covers string methods and the immutability of strings in Python.

# ==========================
# Part 1: Immutability of Strings
# ==========================
# Strings in Python are immutable, which means that once a string is created, it cannot be changed.

a = "!!!!khalid !!!!!!!!!!!!!!!"
print("Original string:", a)
print("Length of string:", len(a))  # len() method returns the length of the string

# ==========================
# Part 2: String Methods
# ==========================
# Strings have various methods that allow you to perform different operations on them.

# Convert all characters to uppercase
print("Uppercase:", a.upper())

# Convert all characters to lowercase
print("Lowercase:", a.lower())

# Remove trailing characters (default is whitespace)
print("Remove trailing '!':", a.rstrip("!"))

# Replace a substring with another substring
print("Replace 'khalid' with 'john':", a.replace("khalid", "john"))

# Split the string into a list using a delimiter
print("Split string by spaces:", a.split(" "))

# Capitalize the first character of the string
blogHeading = "introduction tO js"
print("Capitalized:", blogHeading.capitalize())

# Center align the string within a specified width
str1 = "welcome to the console !!!"
print("Centered string:", str1.center(50))
print("Length of centered string:", len(str1.center(50)))

# Count occurrences of a substring
print("Count of 'a':", a.count("a"))

# Check if the string ends with a specified suffix
print("Ends with '!!!':", str1.endswith("!!!"))
print("Ends with 'to' between index 4 and 10:", str1.endswith("to", 4, 10))

# Find the first occurrence of a substring
print("First occurrence of 'to':", str1.find("to"))

# Check if the string is alphanumeric (contains only letters and numbers)
print("Is alphanumeric:", str1.isalnum())

# Check if the string is alphabetic (contains only letters)
w2 = "welcome"
print("Is alphabetic:", w2.isalpha())

# Check if all characters in the string are lowercase
print("Is lowercase:", w2.islower())

# Check if the string is printable (all characters are printable)
w3 = "welcome\n"
print("Is printable:", w3.isprintable())

# Check if the string contains only whitespace
print("Contains only whitespace:", w3.isspace())

# Check if the string starts with a specified prefix
print("Starts with 'welcome':", w3.startswith("welcome"))

# Swap the case of all characters in the string
print("Swap case:", str1.swapcase())

# Convert the first character of each word to uppercase
print("Title case:", str1.title())

# Check if the string is in title case
print("Is title case:", str1.istitle())

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. The immutability of strings in Python.
# 2. Various string methods such as upper(), lower(), rstrip(), replace(),
# - split(), capitalize(), center(), count(), endswith(), find(), isalnum(),
# - isalpha(), islower(), isprintable(), isspace(), startswith(), swapcase(), and title().


# End of day 4 learning
# Author: Khalid Umar
# Contact: khalid100umar@gmail.com
# Portfolio: https://khalid-umar.com