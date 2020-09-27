#!/usr/bin/env python
# coding: utf-8

# # Phone Loop

# In[ ]:


'''
->Datastructure
    -fullname
    -Phonenumber
    -Email
->Add a new items to a phone
->list items from book
->remove items from book
->search items from book
->store book data to a file
->reload data when we start phone
'''


# In[2]:


phonebook=[]  #list of dictionary
bookitems={'fullname':'', 'number':'', 'email':''}
def add_items(fullname,number,email):
    global phonebook
    item=bookitem.copy()
    item['fullname']=fullname
    item['number']= number
    item['email']=email
    phonebook.append(item)

        # pass or use ... for empty function

def list_items():
    global phonebook
    for item in phonebook:
        print(item)

def cli():
    fullname= input("Enter Name: ")
    number= input("Enter phone number: ")
    email= input("Enter Email: ")
    add_items(fullname, number, email)
        
list_items()

        


# In[4]:


phonebook=[]  #list of dictionary
bookitems={'fullname':'', 'number':'', 'email':''}
def add_items(fullname,number,email):
    global phonebook
    item=bookitem.copy()
    item['fullname']=fullname
    item['number']= number
    item['email']=email
    phonebook.append(item)

        # pass or use ... for empty function

def list_items():
    global phonebook
    for item in phonebook:
        print(item)

def cli():
    fullname= input("Enter Name: ")
    number= input("Enter phone number: ")
    email= input("Enter Email: ")
    add_items(fullname, number, email)
        

cli()
list_items()


# In[ ]:




