#Declare two variables and print that which variable is largest using ternary operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
largest = a if a > b else b
print(f"The larger number is: {largest}")

"""Output
Enter first number: 7
Enter second number: 8
The larger number is: 8
"""
