#!/usr/bin/env python
# coding: utf-8

# #   Iteration 

# In[ ]:


items=["apple","banana","mango"]


# In[2]:


items.extend({"grapes","litchi"})
print(items)


# In[3]:


items.extend({"strawberry":3,"dragon fruit":4})      #only returns keys!! Donot return values in dictionary extending
print(items)


# In[5]:


list({"a","b"})  #returns SETinto List


# In[6]:


list({"a":1,"b":4})   #returns Dictinary into List using list keyword


# In[7]:


list((1,2,3,4))     #returns Tuple into List


# In[8]:


list("kathmandu")     #Each string is iterable


# # For set (to convert list into set)

# In[10]:


a=[1,2,3,4]
b=[3,4,5,6]    
set(a)&set(b)      #Gives intersection value of two list using set keyword


# #  for Dictionary

# In[11]:


print(dict())       #Returns empty dictionary


# In[12]:


dict([("a",3),("b",4),("c",5)])     #Tuple ma xuttai value diyera list ma rakhda key ra value identify garera dictinary ma rakxa


# # key value pair in dictionary

# In[15]:


print(dict(firstname="ram",secondname="kandel"))


# # bool (convert value into boolean) 

# In[16]:


bool(0)     # returns false in 0 else returns true to everyother


# In[17]:


bool(-5)


# In[18]:


bool(3)


# In[19]:


bool(8.8)


# In[20]:


bool(0.0)


# In[21]:


bool(0.1)


# In[23]:


bool("string")


# In[24]:


bool()


# In[25]:


bool(())


# In[26]:


bool([])


# In[27]:


bool({})


# In[ ]:





# # Method

# In[28]:


id("A")


# In[30]:


id("none")


# In[31]:


items=[1,2,3]
dir(items)


# In[32]:


len(items)


# In[34]:


temp=[22.3,45.3,45.31,23.1]
max(temp)


# In[35]:


min(temp)


# In[36]:


sum(temp)


# In[37]:


help(pow)


# In[38]:


pow(3,3)


# In[39]:


help(all)


# In[40]:


all([1,2,3,4])  # if  all true only return true 


# In[41]:


all([0,1,2,3,4])  # if one false all false => bool(0) is false so all is false


# In[42]:


any([0,0,0,1])     # if one true all true


# In[43]:


any([0,0,0,0])   #if all false then return false


# In[3]:


help(input)


# In[ ]:




