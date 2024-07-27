# Input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Swapping without using a third variable
x = x + y
y = x - y
x = x - y

# Display the results
print(f"After swapping: first number = {x}, second number = {y}")
