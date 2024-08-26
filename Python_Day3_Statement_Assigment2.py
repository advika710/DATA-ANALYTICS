#Q2 Using input function take two number and then swap the number
# Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swapping the numbers
num1, num2 = num2, num1

# Printing the swapped numbers
print(f"After swapping: First number = {num1}, Second number = {num2}")

"""
Output:
Enter the first number: 12
Enter the second number: 8
After swapping: First number = 8, Second number = 12
"""
