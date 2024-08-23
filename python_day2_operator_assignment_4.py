#Python program to find the area of a triangle whose sides are given
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"The area of the triangle is: {area}")


"""
Output:
Enter side a: 5
Enter side b: 7
Enter side c: 9
The area of the triangle is: 17.41228014936585
"""
