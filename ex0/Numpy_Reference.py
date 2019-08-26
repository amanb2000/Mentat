#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import numpy as np


# In[12]:


# Making 1-D arrays
arry1 = np.array([1, 2, 3])
print('arry1 is: ',arry1)
print('type: ',type(arry1))
arry1


# In[15]:


# Making 2-D arrays and specifying datatypes
list_in = [[1, 2, 3], [4, 5, 6]]
arry2 = np.array(list_in, dtype='float')
print(arry2)
arry2


# In[18]:


# Converting types:
arry3 = arry2.astype('int')
arry3
# Note: You an also make arrays of type 'object' and have strings and stuff in them!


# In[19]:


# Converting back to lists:
list3 = arry3.tolist()
list3


# In[28]:


# Referencing parts of arrays
arry3[1][:2] # ':' can be read as 'up to but not including' in a zero-indexed system.
             # otherwise it's very similar to regular lists


# In[32]:


# Getting info on arrays:
print('Number of dimensions in arry3:',arry3.ndim)
print('Shape of arry3:',arry3.shape) # linear algebra ordering. Returns tuple.
print('Datatype of arry3:',arry3.dtype)


# In[38]:


# Boolean indexing:
arry_bool = arry3 > 3
print('Parts of arry3 > 3:\n',arry_bool)
print('arry3 at those points: ', arry3[arry_bool])


# In[54]:


# nan and inf: remember that nan and inf are floats...
arry3 = arry3.astype('float')
arry3[0,0] = np.nan
arry3[0,1] = np.inf
arry3


# In[55]:



missing_parts = np.isnan(arry3) | np.isinf(arry3)
arry3[missing_parts] = -1
arry3


# In[118]:


print(arry3.max())
print(arry3.min())

print('Min per column: ',np.amin(arry3, axis=0))
print('Min per row: ', np.amin(arry3, axis=1))


# In[119]:


# Creating new array from existing array
arry3_cpy = arry3.copy()
arry3_notcpy = arry3


# In[120]:


# Flattening
flat = arry3.flatten()
flat


# In[121]:


# np.arange(...) works the same as range() and generates that as an np array.
inArry = np.arange(0, 36)
outArry = inArry.reshape(6, 6)
outArry


# In[122]:


append = np.array([4, 1, 4, 2, 3, 4])
append = append.reshape((1, 6))
outArry = np.concatenate((outArry, append), axis=0)
outArry


# In[123]:


append = np.arange(7)
append = append.reshape((1, append.shape[0]))
append = np.transpose(append)
outArry = np.concatenate((outArry, append), axis = 1)
outArry


# In[126]:


labels = outArry[:, outArry.shape[1]-1]
labels


# In[127]:


outArry = outArry[:, :(outArry.shape[1]-1)]
outArry


# In[128]:


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[129]:


# Model initialization
regression_model = LinearRegression()
# Fit the data(train the model)
regression_model.fit(outArry, labels)
# Predict
y_predicted = regression_model.predict(outArry)


# In[130]:


y_predicted


# In[131]:


regression_model


# In[ ]:




