# Input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Swapping using a third variable
temp = x
x = y
y = temp

# Display the results
print(f"After swapping: first number = {x}, second number = {y}")
