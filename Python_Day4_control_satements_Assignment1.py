#Q1 Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is divisible by 2
if number % 2 == 0:
    # If true, print "Even"
    print("The number is Even")
else:
    # If false, print "Odd"
    print("The number is Odd")

"""
Output:
Enter a number: 70
The number is Even

Enter a number: 57
The number is Odd
"""
