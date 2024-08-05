#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1 Write a program for arithmatic operators

# Arithmetic Operators
a = 10
b = 5

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Floor Division: {a} // {b} = {a // b}")


# In[2]:


#Q.2 Write a program for assignment operators

# Assignment Operators
a = 10
print(f"Initial value of a: {a}")

a += 5
print(f"After a += 5: {a}")

a -= 3
print(f"After a -= 3: {a}")

a *= 2
print(f"After a *= 2: {a}")

a /= 4
print(f"After a /= 4: {a}")

a %= 3
print(f"After a %= 3: {a}")

a **= 2
print(f"After a **= 2: {a}")

a //= 2
print(f"After a //= 2: {a}")


# In[3]:


#Q.3Write a program for Bitwise operators 

# Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(f"Bitwise AND: {a} & {b} = {a & b}")
print(f"Bitwise OR: {a} | {b} = {a | b}")
print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
print(f"Bitwise NOT: ~{a} = {~a}")
print(f"Bitwise LEFT SHIFT: {a} << 2 = {a << 2}")
print(f"Bitwise RIGHT SHIFT: {a} >> 2 = {a >> 2}")


# In[7]:


# Program to find the greatest of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if (num1 == num2) and (num1 == num3):
   print("all num are same")
elif (num2 == num1) and (num2 <num3):
    print("num1 and num2 are equal and num3 is greatest")
elif(num3==num2) and (num3<num1):
    print("num3 and num2 are equal and num1 is greatest")
   
else:
     if (num1 >= num2) and (num1 >= num3):
        greatest = num1
     elif (num2 >= num1) and (num2 >= num3):
        greatest = num2
     else:   
        greatest = num3

print(f"The greatest number is: {greatest}")


# In[9]:


import math

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius**2

# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Function to calculate the area of a square
def area_of_square(side):
    return side**2

# Main function to interact with the user
def main():
    print("Choose the shape to calculate its area:")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Square")
    
    choice = int(input("Enter your choice (1/2/3/4): "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = area_of_circle(radius)
        print(f"The area of the circle with radius {radius} is: {area}")
    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_of_triangle(base, height)
        print(f"The area of the triangle with base {base} and height {height} is: {area}")
    elif choice == 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_of_rectangle(length, width)
        print(f"The area of the rectangle with length {length} and width {width} is: {area}")
    elif choice == 4:
        side = float(input("Enter the side length of the square: "))
        area = area_of_square(side)
        print(f"The area of the square with side length {side} is: {area}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()



# In[ ]:




