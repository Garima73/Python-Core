#!/usr/bin/env python
# coding: utf-8

# In[3]:


a= None      
a is None     # none le exactly tei value ho ki hoena check garxaaia


# In[4]:


a is True


# In[5]:


a is False  # because a is neither true nor false!! it is none


# In[ ]:


# if sanga in keyword aayo vane chahi in le condition check garxa

#continue le continue vanda jadaina again loop ma janxa

#While TRUE RAKHDA infinite loop ma janxa

#break le immediate paarent loop lai break garxa eg: while{if:break} xa vane while(parent loop) lai break garxa


# In[7]:


'Ktm' in ['Ktm', 'pkr']


# In[10]:


def say_hello(recipient):
    return 'Hello, {}!'.format(recipient)
say_hello('World!!')


# In[ ]:


import numpy as np

def square(x):
    return x*x


# In[12]:


x=np.random.randint(1,10)
y=square(x)
print("%d sqaure is %d"%(x.y))


# In[ ]:




