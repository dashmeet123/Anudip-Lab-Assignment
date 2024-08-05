#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Taking input from user
number = int(input("Enter a number: "))
check_even_odd(number)


# In[2]:


#2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age

def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote yet.")

# Taking input from user
age = int(input("Enter your age: "))
check_voting_eligibility(age)


# In[3]:


#3. Write a Python program that determines if a given year is a leap year or not.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Taking input from user
year = int(input("Enter a year: "))
is_leap_year(year)




# In[4]:


#4.Create a Python program that checks if a user-given number is positive, negative, or zero.

def check_number(num):
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print("The number is zero")

# Taking input from user
number = float(input("Enter a number: "))
check_number(number)


# In[5]:


#5.Write a Python program that determines the largest of three numbers entered by the user.

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    print(f"The largest number is: {largest}")

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
find_largest(num1, num2, num3)


# In[ ]:




