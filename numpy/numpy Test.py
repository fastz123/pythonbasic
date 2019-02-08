
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


#column vector
c = np.array([1,2,3])
print(c.shape)

print(c[0])


# In[6]:


#row vector
r = np.array([[1,2,3]])
print(r.shape)


# In[7]:


#obtaining a particular entry
print(r[0,1])


# In[8]:


#creating a matrix with all zeros
a = np.zeros((2,2))
print(a)

#creating a matrix filled with the same constant
c = np.full((2,2),7)
print(c)

#creating a matrix with random values
d = np.random.random((2,2))
print(d)


# In[14]:


#creating a matrix
A = np.array([[1,2,3,4],[5,6,7,8]])
print(A)


# In[11]:


B = np.array([[11,12,13,14],[15,16,17,18]])
B


# In[15]:


A=A.T


# In[16]:


np.dot(A,B)


# In[17]:


#coefficient matrix A and a vector b
A = np.array([[60,5.5,1],[65,5.0,0],[55,6.0,1]])
b = np.array([[66,70,78]])


# In[18]:


eye3 = np.eye(3)
eye3


# In[20]:


#computing ana inverse matrix
from numpy.linalg import inv
A_inv = inv(A)
A_inv


# In[21]:


#wrong multiplication
A*A_inv


# In[22]:


A.dot(A_inv)


# In[25]:


#solution of a linear system
x = A_inv.dot(b.T)
x


# In[27]:


#better way to solve the same linear system
from numpy.linalg import solve
x = solve(A,b.T)
x

