# day3.py
# This script covers strings, multiline strings, index errors, string slicing, and negative slicing.

# ==========================
# Part 1: Strings
# ==========================
# Strings are sequences of characters enclosed in single, double, or triple quotes.

# Example of strings
single_quote_string = 'Hello, Python!'
double_quote_string = "Hello, Python!"
triple_quote_string = """Hello,
Python!"""

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)

# ==========================
# Part 2: Multiline Strings
# ==========================
# Multiline strings can be created using triple quotes. They can span multiple lines.

multiline_string = """This is a multiline string.
It spans multiple lines.
You can write as much as you want here."""
print(multiline_string)

# ==========================
# Part 3: Index Error
# ==========================
# Strings are indexed, and you can access characters using their index. The index starts from 0.
# Trying to access an index that doesn't exist will raise an IndexError.

sample_string = "Python"
print("Character at index 0:", sample_string[0])  # First character
print("Character at index 5:", sample_string[5])  # Last character

# Uncomment the line below to see the IndexError
# print("Character at index 6:", sample_string[6])  # This will raise an IndexError

# ==========================
# Part 4: String Slicing
# ==========================
# Slicing allows you to get a substring from a string. The syntax is string[start:end].

# Example of string slicing
substring = sample_string[0:4]  # Gets characters from index 0 to 3 (end index is not included)
print("Substring from index 0 to 3:", substring)

# Slicing with default start and end
print("Substring from start to index 3:", sample_string[:4])  # From start to index 3
print("Substring from index 2 to end:", sample_string[2:])  # From index 2 to end
print("Full string using slicing:", sample_string[:])  # Full string

# ==========================
# Part 5: Negative Indexing and Slicing
# ==========================
# Negative indexing allows you to access characters from the end of the string.

# Example of negative indexing
print("Last character using negative indexing:", sample_string[-1])  # Last character
print("Second last character using negative indexing:", sample_string[-2])  # Second last character

# Negative slicing
print("Substring using negative slicing:", sample_string[-6:-2])  # From index -6 to -2
print("Substring from start to -2:", sample_string[:-2])  # From start to index -2
print("Substring from -4 to end:", sample_string[-4:])  # From index -4 to end

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Strings and how to create them.
# 2. Multiline strings using triple quotes.
# 3. Index errors and how to avoid them.
# 4. String slicing to get substrings.
# 5. Negative indexing and slicing to access characters from the end of the string.

# End of day 3 learning


# Author: Khalid Umar
# Contact: khalid100umar@gmail.com
# Portfolio: https://khalid-umar.com