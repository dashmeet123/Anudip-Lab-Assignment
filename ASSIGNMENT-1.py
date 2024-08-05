#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1 print helloworld

print('Hello World')


# In[3]:


#Q.2 describe local variable and global variable code
#local variable
def f():
    s="Hey Python"
    print(s)

    
f()

#global variable

def f():
    print("inside",s)

s="Dashmeet Singh"
f()
print("outside",s)


# In[4]:


# Q.3 Write a code that describe Indentation error

a=10
b=14
if (a>b):
print('true')


# In[5]:


#Q.4 write a code that describe local and global variable with same name

var = " global variable"

def f1():
    # Local variable
    var = "local variable"
    print(var)

# Call the function
f1()

# Print the global variable
print( var)


# In[6]:


#Q.5 Write a code for string, int and float input.

#Write a code for string, int and float input.
# Take string input
string_input = input("Enter a string: ")

# Take integer input
int_input = int(input("Enter an integer: "))

# Take float input
float_input = float(input("Enter a float: "))

# Print the inputs
print(f"String input: {string_input}")
print(f"Integer input: {int_input}")
print(f"Float input: {float_input}")


# In[ ]:




