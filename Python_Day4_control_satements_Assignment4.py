#Q4 Create a Python program that checks if a user-given number is positive, negative, or zero.

# Prompt the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is greater than 0
if number > 0:
    # If true, print "Positive"
    print("The number is Positive")
# Check if the number is less than 0
elif number < 0:
    # If true, print "Negative"
    print("The number is Negative")
else:
    # If neither, print "Zero"
    print("The number is Zero")
    
"""
Output:

Enter a number: -2
The number is Negative

Enter a number: 71
The number is Positive
 
Enter a number: 0
The number is Zero
"""
