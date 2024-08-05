#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1. Function with Parameters:

def personalized_greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


personalized_greet("Alice", 30)


# In[6]:


#2.Function without Parameter:
def greet():
    print("Hello, World!")

# Calling the function
greet()


# In[7]:


#3.Function with Default Parameter:

def greet(name="Guest", age=25):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with both arguments
greet("Alice", 30)

# Calling the function with one argument
greet("Bob")

# Calling the function with no arguments
greet()


# In[8]:


#4.Function with Return Keyword:

def sum():
    a=1
    b=2
    sum=a+b
    return sum

sum()


# In[9]:


#a) WAP to print factorial value of a given number using recursion.

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}.")


# In[11]:


# b) WAP to display Fibonacci series up to 10 iteration using recursion.

def fibonacci(num):
    
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
term=10
fibonacci_series=[]

for i in range(term):
    fibonacci_series.append(fibonacci(i))

print("Fibonacci series up to 10 terms:", fibonacci_series)


# In[ ]:




