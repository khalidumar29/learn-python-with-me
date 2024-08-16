# For Loop with Else Statement

# Example of a for loop with an else statement
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    # This will not execute because the loop was terminated by a break statement
    print("Loop executed completely")

# Example of a while loop with an else statement
i = 7
while i < 7:
    print(i)
    i += 1
    break
else:
    # This will not execute because the loop condition is false and the loop didn't run
    print("This will not be printed")

# Multiplication Table with Error Handling
a = input("Enter a number: ")

try:
    print(f"Multiplication table of {a} is:")
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a) * i}")
except ValueError:
    # Handle the case where the input is not a valid number
    print("Please enter a valid number")

# End of the program
print("some imp lines code")
print("End of the program")
