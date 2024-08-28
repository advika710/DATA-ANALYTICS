#Q5 Write a Python program that determines the largest of three numbers entered by the user.

# Prompt the user to enter the first number
num1 = float(input("Enter first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter second number: "))

# Prompt the user to enter the third number
num3 = float(input("Enter third number: "))

# Check if the first number is greater than or equal to the second and third numbers
if num1 >= num2 and num1 >= num3:
    # If true, assign the first number to the variable 'largest'
    largest = num1
# Check if the second number is greater than or equal to the first and third numbers
elif num2 >= num1 and num2 >= num3:
    # If true, assign the second number to the variable 'largest'
    largest = num2
else:
    # If neither, assign the third number to the variable 'largest'
    largest = num3

# Print the largest number
print(f"The largest number is {largest}")

"""
Output:

Enter first number: 100
Enter second number: 205
Enter third number: 1000
The largest number is 1000.0
"""
