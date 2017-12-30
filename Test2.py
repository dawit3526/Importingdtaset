
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





