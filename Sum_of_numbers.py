#!/usr/bin/env python
# coding: utf-8

# Provide a number as a start point and a second number as an end point and find the sum of all numbers in between.

# In[3]:


first = int(input("Please enter an number:   "))
last = int (input("Please enter another number:   "))
total = 0
for number in range (first,last+1):
    total += number
print (total)


# In[4]:


first1 = input("Please enter an number:   ")
last1 =  input("Please enter another number:   ")
total = 0
for number in range (int(first1),int(last1)+1):
    total += number
print (total)


# In[ ]:




