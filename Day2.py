#!/usr/bin/env python
# coding: utf-8

# # Strings and indexing

# In[2]:


city= "kathmandu nepal"
city[0]


# In[3]:


city[5]


# In[4]:


len(city)


# In[5]:


city[len(city)-1]


# In[6]:


city[-1]


# In[7]:


city[-3]


# # Slicing (start-include, end-exclude)

# In[8]:


city="Chitwan Nepal"
city[0:5]


# In[9]:


city[0:9]


# In[10]:


city[:]


# In[11]:


city[:4]


# In[12]:


city[7:]


# In[13]:


city[: :2]


# In[15]:


city[: :-2]


# In[16]:


city[-1::-2]


# In[17]:


city[-1: :-1] # =>String Reverse[-1:0:-1]


# In[23]:


city.lower() # Convert upper case into lower case 


# In[21]:


city.upper()


# In[22]:


city.capitalize() #make first letter capital


# # Boolean( return true or false)

# In[24]:


city.startswith("k")


# In[26]:


city.startswith("chi")


# In[27]:


city.startswith("ctwn")


# In[28]:


city.startswith("C") #Reject upper case also


# In[29]:


city.endswith("c")


# In[30]:


city.endswith("pal")


# # Data Structures 

# # 1. LIST

# In[33]:


city=["ktm","pkr","chtwn"]
print(city)


# In[37]:


items=["pkr",["ktm","chitwn","bhktapur"],"siraha"]
print(items[1])


# In[43]:


print(items[1:2])


# In[47]:


print(items[-1])


# In[48]:


items.append("lalitpur")    #To add items
print(items)


# In[49]:


items.add("basantapur")
print(items)


# In[12]:


items=["pkr",["ktm","chitwn","bhktapur"],"siraha"]
print(items[0:2:-1])


# In[13]:


items=["pkr",["ktm","chitwn","bhktapur"],"siraha"]
print(items[2:1:-1])


# In[20]:


items=["pkr",["ktm","chitwn","bhktapur"],"siraha"]  #Replace the value
items[1]="madi"
print(items)


# In[19]:


items=["pkr","ktm","siraha"]
items[2]="madi"
print(items)


# In[27]:


items=['a','b','c']            #Extend the value
items.extend(['d','e','d'])
print(items)


# In[28]:


items.count("d")


# In[31]:


items.reverse()
print(items)


# In[32]:


items.sort()
print(items)


# In[34]:


items.pop()              #Removes Last Item
print(items)


# In[35]:


items.reverse()
print(items)


# In[36]:


items.pop()
print(items)


# In[2]:


items=['a','b','c','d','e','d']            #Extend the value

items.pop(1)
print(items)


# In[37]:


items.append("a","e","i","o","u")
print(items)


# In[40]:


items.extend("a","e","i","o","u")
print(items)


# In[41]:


help(items.remove)


# In[5]:


items=['a','b','c','d','e','d']            #Remove the first value

items.remove("d")
print(items)


# # 2.TUPLE

# In[44]:


city_tuple=("ktm","pkr","chitwn")  #we cannot append items in TUPLE
print(city_tuple)


# In[7]:


city_tuple=("ktm","pkr","chitwn")
city_tuple.append("basantapur")
print(city_tuple)


# In[15]:


city_tuple=("ktm","pkr","chitwn")
city_tuple.add("basantapur")
print(city_tuple)


# In[16]:


city_tuple=("ktm","pkr","chitwn")
city_tuple[2]


# In[21]:


city_tuple=("ktm","pkr","chitwn")  #Tuple does not support replacing method
city_tuple[2]="madi"
print(city_tuple)


# # 3.SET

# In[3]:


city_set={"ktm","pkr","chtwn"} # we cannot index value in set eg: city_set[1]
print(city_set)


# In[5]:


city_set={"ktm","pkr","chtwn"}
city_set.add("basantapur")
print(city_set)


# In[6]:


city_set={"ktm","pkr","chtwn"}
city_set.append("basantapur")
print(city_set)


# In[14]:


city_set={"ktm","pkr","chtwn"}
city_set[2]


# # METHODS

# # 1.dir()

# In[23]:


city="a,b,c"
dir(city)


# In[25]:


help(city.translate)


# In[26]:


dir(all)


# # 4.DICTIONARY (have keys and values)

# In[7]:


student={"name":"ram", "age":12, "address":"ctwn"}
help(student)


# In[8]:


dir(student)


# In[9]:


student={"name":"ram", "age":12, "address":"ctwn"}
print(student)


# In[13]:


student["phone number"]=123456789      #Add the value without using append
print(student)


# In[14]:


student["age"]=14     #Update a single value
print(student)


# In[16]:


student.update({"name": "harry","friends":["ron","bipul"]})      #Update more than single value
print(student)


# In[17]:


student.keys()


# In[18]:


student.values()


# In[19]:


student.items()     #gives value in the form of tuple(list of tuple)


# In[20]:


student.get("name")


# In[22]:


student.get("pet")   #It returns none


# In[25]:


student.get("pet","dog")


# In[26]:


student.get("pet","dog")
print(student)


# # OPERATORS

# #  1. In List

# In[32]:


lst1=["I "+ "Have"]    #concatenate 2 LISTS
lst2=[str(12) + " pens"]
lst=lst1+lst2
print(lst)


# #  2. In Tuple

# In[33]:


("12", "10")+ ("33", "44")   # concatenate 2 TUPLES


# # 3. In set

# In[34]:


{1,2,3}+ {4,5,6}   #concatination cannot be done in SET


# In[38]:


a={1,2,3,4,5}    # Gives Intersection value
b={3,4,5}
print(a&b)


# In[39]:


a={1,2,3,4,5}    # Gives Intersection value
b={3,4,5}
print(a.intersection(b))


# In[40]:


dir(a)


# In[41]:


a.issubset(b)


# In[44]:


b.difference(a)


# # 4. IN DICTIONARY

# In[35]:


{"a":1} + {"b":2} #concatination cannot be done in DICTIONARY

