#!/usr/bin/env python
# coding: utf-8

# # '''Generate fibonacci value upto 100'''  "'=>comment for long

# In[1]:


a,b=0,1
print(a)
print(b)
while b<100:
    c=a+b
    a=b
    b=c
    print(c)
print("value is =>",c)    


# In[16]:


a,b=0,1
print(a)
while(b<100):
    print(b)
    a,b=b,b+a
print("The final value is: =>",b)    
    


# In[24]:


a,b=0,1
for i in range(100):
    print("{} => {}".format(i,b))
    a,b = b,b+a


# In[3]:


till= input("Enter a number..")
print(till)
for num in range(1,int(till) + 1):
    if num %3 ==0:
        if num %5 ==0:
            print("FooBar")
        else:
            print("Foo")
    else:
        if num % 5==0:
            print("Bar")
        else:
            print(num)


# In[6]:


till= input("Enter a number..")
print(till)
for num in range(1,int(till) + 1):
    if num %3 ==0 and num %5==0:
        print("Foobar")
    elif num%3==0:
        print("Foo")
    elif num%5==0:
        print("Bar")
    el:
        print(num)


# In[ ]:


print(5)


# # Conditions

# In[25]:


3>2 and 3>1


# In[27]:


3>4 or 3>1


# In[ ]:


till= input("Enter a number..")
print(till)
for num in range(1,int(till) + 1):
    if num %3 ==0:
        if num %5 ==0:
            print("FooBar")
        else:
            print("Foo")
    else:
        if num % 5==0:
            print("Bar")
        else:
            print(num)


# # Function
# 

# In[8]:


def foobar():
    till= input("Enter a number..")
   
    for num in range(1,int(till) + 1):
        if num %3 ==0:
            if num %5 ==0:
                print("FooBar")
            else:
                print("Foo")
        else:
            if num % 5==0:
                print("Bar")
            else:
                print(num)
                
foobar()


# In[11]:


from Day4.ipynb import foobar


# In[ ]:


till= input("Enter a number..")
def foobar():
    nonlocal till      #It represent till is not local(not inside of function) and it is from outside; we can abstract it and use it
    for num in range(1,int(till) + 1):
        if num %3 ==0:
            if num %5 ==0:
                print("FooBar")
            else:
                print("Foo")
        else:
            if num % 5==0:
                print("Bar")
            else:
                print(num)
                
foobar()


# #  Function using argument

# In[14]:


till= input("Enter a number..")
def foobar(upto):  # argument is passed
   for num in range(1,int(upto) + 1):
       if num %3 ==0:
           if num %5 ==0:
               print("FooBar")
           else:
               print("Foo")
       else:
           if num % 5==0:
               print("Bar")
           else:
               print(num)
               
foobar(till) #parameter is passed


# In[15]:


import math
math.pi


# In[14]:


def bac(y):
    print("Entered number is:",y)
    
def abc():
    global x
    x=int(input("Enter item:"))
    return x
abc()
bac(x)


# In[15]:


def xyz(x):
    print(x)
    print("Thank You!!")
xyz("Hello World")


# In[3]:


'''
height, weight,age
'''
def bmi_calc(name,height,weight):
    BMI=weight/(height**2)
    if BMI<25:
        print(name + "is not overweight")
    else:
        print(name + "is overweight")
        
def entry():
    global result
    x=input("Enter your Name: ")
    y=input("Enter your Height: ")
    z=input("Enter your weight: ")
    bmi_calc(x,y,z)

entry()


    
    


# In[ ]:




