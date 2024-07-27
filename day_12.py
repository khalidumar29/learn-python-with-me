# day12.py
# This script covers recursion and sets in Python.

# ==========================
# Part 1: Recursion
# ==========================
# Recursion is a process where a function calls itself directly or indirectly.

# Example of a recursive function to calculate factorial
def factorial(n):
    """Return the factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Example of a recursive function to calculate Fibonacci numbers
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci number at position 2: {fibonacci(2)}")

# ==========================
# Part 2: Sets
# ==========================
# Sets are unordered collections of unique items.

# Creating and printing a set
s = {1, 2, 3, 4, 5, 5}
print("Set with unique elements:", s)

# Creating an empty set
khalid = set()
print("Type of khalid:", type(khalid))

# Set methods

# Union
s = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Union of s and s2:", s.union(s2))
s.update(s2)
print("Updated s with union of s2:", s)

# Intersection
cities = {"Lagos", "Abuja", "Kano", "Kaduna"}
cities2 = {"Kano", "Kaduna", "Jos", "Enugu"}
print("Intersection of cities and cities2:", cities.intersection(cities2))
cities.intersection_update(cities2)
print("Updated cities with intersection of cities2:", cities)

# Symmetric Difference
print("Symmetric difference between cities and cities2:", cities.symmetric_difference(cities2))
cities.symmetric_difference_update(cities2)
print("Updated cities with symmetric difference of cities2:", cities)

# Disjoint sets
print("Are cities and cities2 disjoint?", cities.isdisjoint(cities2))

# Superset and Subset
print("Is cities a superset of cities2?", cities.issuperset(cities2))
print("Is cities a subset of cities2?", cities.issubset(cities2))

# Remove and Discard
cities.remove("Kano")
print("Cities after removing 'Kano':", cities)
cities.discard("Kaduna")
print("Cities after discarding 'Kaduna':", cities)

# Pop
cities.pop()
print("Cities after popping an element:", cities)

# Delete and Clear
del cities
cities2.clear()
print("Cities2 after clearing:", cities2)

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Recursion: including examples of calculating factorial and Fibonacci numbers.
# 2. Sets: including creation, methods for union, intersection, symmetric difference, disjoint sets, superset, subset, and various set operations.

# End of day 12 learning
