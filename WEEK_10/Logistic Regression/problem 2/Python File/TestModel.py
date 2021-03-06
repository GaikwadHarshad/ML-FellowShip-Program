#!/usr/bin/env python
# coding: utf-8

# In[38]:


# import libraries
import numpy as  np
import pandas as pd
import  array
import matplotlib.pyplot as plt
import importlib.util
from matplotlib.colors import ListedColormap
import array
from  sklearn.preprocessing import LabelEncoder
import sklearn
import pickle
from sklearn.metrics import confusion_matrix
import warnings
import csv
warnings.filterwarnings('ignore')


# In[39]:


# importing template file 
spec = importlib.util.spec_from_file_location("Template", "/home/admin1/PycharmProjects/Basic Python/myprograms/WEEK_10/UtilityTemplate/UtilTemplate.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
# creating object of Template class
log_template = foo.Template()


# In[40]:


# load dataset
test_dataset = log_template.read_csv('CSV_Files/test.csv')
print("Dataset has {} rows and {} Columns".format(test_dataset.shape[0],test_dataset.shape[1]))


# In[41]:


# load model training
file = open('Pickle File/TrainPickle.pkl', 'rb')
classifier = pickle.load(file)
scaling =  pickle.load(file)


# In[42]:


# seperate label and features
x_test =  test_dataset.iloc[:,:-1].values
y_test = test_dataset.iloc[:,8].values
# x.shape,y.shape


# In[43]:


x_test = pd.DataFrame(x_test)
type(x_test)


# In[44]:


# one hot encoding on x data
x_test = log_template.one_hot_encode(x_test)


# In[45]:


# encode dependent variable      
label_encoder_y = LabelEncoder()
y_test = label_encoder_y.fit_transform(y_test)


# In[46]:


# perform transform on test data
x_test = scaling.transform(x_test)
x_test.shape


# In[47]:


# prediction on model by test data
prediction =  log_template.prediction(x_test, classifier)


# In[48]:


# confusion matrix for describe performance of classification model
cfm_test = sklearn.metrics.confusion_matrix(y_test,prediction)


# In[49]:


# get accuracy
accuracy =  sklearn.metrics.balanced_accuracy_score(y_test,prediction)*100
print("Test Accuracy:",accuracy)


# In[ ]:




