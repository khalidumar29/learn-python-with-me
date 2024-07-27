# day9.py
# This script covers lists and tuples in Python.

# ==========================
# Part 1: Lists
# ==========================
# Lists are mutable, ordered collections of items.

# Creating and printing a list
l = [1, 2, 3, 4]
print("Original list:", l)

# Appending an item to the list
l.append(5)
print("List after appending 5:", l)

# Sorting and reversing a list
l = [7, 5, 9, 11, 13, 9, 7]
l.sort(reverse=True)  # Sort in descending order
print("List after sorting in descending order:", l)
l.reverse()  # Reverse the list
print("List after reversing:", l)

# Index and count of an item in the list
print("Index of 9:", l.index(9))
print("Count of 9:", l.count(9))

# Copying and modifying a list
m = l.copy()
m[0] = 0
m.insert(1, 20)
print("Original list:", l)
print("Modified copy of the list:", m)

# ==========================
# Part 2: Tuples
# ==========================
# Tuples are immutable, ordered collections of items.

# Creating and printing a tuple
tup = (1,)  # Single element tuple
print("Single element tuple:", tup)
tup = (1, 2, 3, 4, 5, 6, "green")
print("Tuple:", tup)
print("Type of tup:", type(tup))

# Checking for an item in the tuple
if "green" in tup:
    print("Yes, 'green' is in the tuple")

# Slicing a tuple
print("Slicing tup from index 1 to 5:", tup[1:5])
print("Slicing tup from index 1 to 5 with step 2:", tup[1:5:2])
print("Slicing tup from index 1 to 5 with step -1:", tup[1:5:-1])
print("Slicing tup from index 5 to 1 with step -1:", tup[5:1:-1])

# ==========================
# Part 3: Tuple Manipulation
# ==========================
# Although tuples are immutable, you can convert them to a list to manipulate and then convert back to a tuple.

countries = ("India", "USA", "UK", "Canada", "Australia")
print("Original tuple:", countries)

# Convert tuple to list to manipulate
temp = list(countries)
temp.append("Germany")  # Append an item
temp.pop(3)  # Remove the item at index 3
countries = tuple(temp)  # Convert back to tuple
print("Modified tuple:", countries)

# Multiple length of tuple (tuple repetition)
print("Tuple repeated twice:", countries * 2)

# ==========================
# Summary
# ==========================
# In this script, we covered:
# 1. Lists: creation, modification, sorting, reversing, indexing, counting, and copying.
# 2. Tuples: creation, slicing, checking for items, and manipulation by converting to list and back to tuple.
# 3. Tuple repetition using the multiplication operator.

# End of day 9 learning
