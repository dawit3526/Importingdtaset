
# coding: utf-8

# In[1]:

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


# In[22]:

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target =data['target']
feature_names
features[:10]
labels =list(data.target_names)


# In[11]:


for t,marker,c in zip(xrange(3),">ox","rgb"):
# We plot each class on its own to get different colored markers
    plt.scatter(features[target == t,0],
    features[target == t,1],
    marker=marker,
    c=c)
plt.show()


# In[23]:

plength = features[:,2]
len(plength)
is_setosa = (labels == 'setosa')
max_setosa = 


# In[ ]:



