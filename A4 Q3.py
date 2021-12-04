#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Write a Python program to square the elements of a list using map() function.



#Sample List: [4, 5, 2, 9]

#Square the elements of the list:

#[16, 25, 4, 81]

def square_num(a):
    return a**2
print("Sample list:[4, 5, 2, 9]")
print("Squared_numbers_are:")
print(list(map(square_num,[4, 5, 2, 9])))


# In[ ]:




