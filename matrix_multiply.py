
# coding: utf-8

# In[23]:


## works with any two matrices
def multiply_matrices(A, B):
    row = []
    matrix = []
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            sums = 0
            for k in range(len(B)):
                sums = sums + (A[i][k]*B[k][j])
            row.append(sums)
        matrix.append(row)
        row = []
    return matrix


# In[24]:


import numpy as np

A = [[1, 1], [0,1]]
B = [[12,6], [4,5]]

multiply_matrices(A,B)


# In[20]:


## check solution with numpy
np.matmul(A,B)

''' output: array([[16, 11], [ 4,  5]])'''


# In[25]:


A = [[0, 0], [0,0]]
B = [[12,6], [4,5]]

multiply_matrices(A,B)


''' output: array([[0, 0], [0, 0]])'''


# In[26]:


A = [[50, 2], [3,75]]
B = [[3,12], [4,1]]

multiply_matrices(A,B)


# In[28]:


np.matmul(A,B)

