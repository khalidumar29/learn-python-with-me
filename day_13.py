# Dictionary Basics and Operations

# Creating a dictionary with different types of keys and values
dic = {
    "name": "John",      # String key with string value
    "age": 30,           # String key with integer value
    "city": "New York",  # String key with string value
    786: "hello"         # Integer key with string value
}

# Accessing values using keys
print(dic[786])  # Output: hello
print(dic.get("name"))  # Output: John

# If a key does not exist, `get()` returns None instead of raising an error
print(dic.get("name1"))  # Output: None

# Getting all the keys from the dictionary
print(dic.keys())  # Output: dict_keys(['name', 'age', 'city', 786])

# Iterating through the dictionary keys and printing corresponding values
for key in dic:
    print(dic[key])

# Getting all key-value pairs as a list of tuples
print(dic.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), (786, 'hello')])

# Two example dictionaries
ep1 = {
    122: 45,
    123: 56,
    124: 67,
    125: 78,
    126: 89,
}

ep2 = {
    222: 45,
    223: 56,
    224: 67,
    225: 78,
}

# Dictionary Operations

# Removing a key-value pair using `pop()`
ep1.pop(122)  # Removes the key 122 from ep1

# Removing the last inserted key-value pair using `popitem()`
ep1.popitem()  # Removes the last item (126: 89) from ep1

# Deleting a specific key-value pair using `del`
del ep1[123]  # Removes the key 123 from ep1

# Printing the modified dictionary
print(ep1)  # Output: {124: 67, 125: 78}

# Creating a copy of a dictionary
ep1_copy = ep1.copy()  # Creates a shallow copy of ep1

# Clearing all items from the copied dictionary
ep1_copy.clear()  # Now ep1_copy is empty

print(ep1_copy)  # Output: {}

# You can also update a dictionary with another dictionary or iterable of key-value pairs.
ep1.update(ep2)  # Updates ep1 with the key-value pairs from ep2
print(ep1)  # Output: {124: 67, 125: 78, 222: 45, 223: 56, 224: 67, 225: 78}
