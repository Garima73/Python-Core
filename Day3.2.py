#!/usr/bin/env python
# coding: utf-8

# # Iteration(For,while)

# # 1.For

# In[1]:



for items in[1,2,3]:
    print(items)


# In[2]:


temp=[22.1,23.4,33.5]
for each in temp:
    print(temp)


# In[3]:


temp=[22.1,23.4,33.5]
for each in temp:
    print(each)


# In[9]:


error=0.5
temp=[22.1,23.4,33.5]
for each in temp:
    print(each,each + error)


# In[10]:


for each in temp:
       print("Original Temperature: " + str(each) + " Corrected Temperature: " + str(each+error))


# In[11]:


phone=["iphone","samsung","nokia"]
for each in phone:
    print(each)


# In[12]:


phone=["iphone","samsung","nokia"]
for each in phone:
    print(phone)


# In[13]:


phone=("iphone","samsung","nokia")
for each in phone:
    print(each)


# In[14]:


phone={"iphone","samsung","nokia"}
for each in phone:
    print(each)


# In[18]:


phone={"iphone":1,"samsung":2,"nokia":3}
for each in phone:
    print(each)


# In[27]:


phone={"iphone":1,"samsung":2,"nokia":3}

for each in phone.values():
    print(each)
 


# In[28]:


for key in phone:
    print(key,phone[key])     #Retuns both key and values


# In[30]:


phone["samsung"]   #gives values


# In[32]:


phone.items()   #returns dictonary in form of tuple


# In[33]:


for each in phone.items():    #returns tuple
    print(each)


# In[34]:


for each in[(1,2),(2,3),(3,4)]:    #list vitra item ma loop lagako!! 
    print(each)


# In[37]:


airport=[("ktm","Kathmandu"),("lka","Lukla"),("chtwn","Chitwan"),("bhhawa","Bhairahawa")]
for airports in airport:
    print(airports,"****")


# In[39]:


for airports in airport:
    print(airports, type(airports))


# In[45]:


for airports in airport:
    print(airports[0], "=>", airports[1])


# In[61]:


for airports in airport:
    print("The code of {} is: {}".format(airports[1], airports[0]))


# In[60]:


airport=[("ktm","Kathmandu"),("lka","Lukla"),("chtwn","Chitwan"),("bhhawa","Bhairahawa")]
for airports in airport:
    code,city=airports[0],airports[1]
    print("The code value of {} is => {}".format(city,code))


# In[59]:


for  code,city in airport:            #code, city tuple ko rup ma act garxa. code le first index ra city le second index herxa
    print("The code value of {} is => {}".format(city,code))  


# In[55]:


print(airport)


# In[56]:


dic=dict(airport)


# In[57]:


print(dic)       #convert tuple into dictionary


# In[58]:


dic.items()   #returns list of tuples


# In[64]:


for key,values in dic.items():
     print("The code value of {} is => {}".format(values,city))


# In[67]:


for key in dic:
     print("The code value of {} is => {}".format(dic[key],key))


# # Range

# In[73]:


range(20)


# In[74]:


for i in range(20):
    print(i)


# In[75]:


range(1,10,2)  #(starts,end,interval)


# In[76]:


for i in range(1,10,2):
    print(i)


# In[77]:


list(range(1,10,2))   #list is iterable so range directly halna milxa


# In[2]:


result=[]
for i in range(1,30):
    if i % 3 == 0:
        result.append(i)
print(result)
    


# # While Loop

# In[68]:


a=5
while(a<10):
    print(a)
    a=a+1  #can also use as a+=1


# In[70]:


a*=2
print(a)


# In[72]:


a/=3
print(a)


# In[3]:


if True:
    print("yes")


# In[4]:


if False:        #It returns nothing
    print("yes")


# In[ ]:




