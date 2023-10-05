#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# # Upload Dataset

# In[2]:


data = pd.read_csv("apple_products.csv")


# In[3]:


data


# # check missing value

# In[4]:


print(data.isnull().sum())


# In[10]:


print(data.isnull())


# # Calculate Standard Deviation

# In[5]:


print(data.describe())


# In[6]:


data.describe()


# # Top 10 i phone sales analysis in india

# In[7]:


highest_Rated = data.sort_values(by = ["Star Rating"],ascending = False)
a = highest_Rated.head(10)
print(a['Product Name'])


# # No. of ratings of the highest rated i phone on flipcart

# In[8]:


iphones = highest_Rated["Product Name"].value_counts()
labels = iphones.index
counts = highest_Rated["Number Of Ratings"]
figure = px.bar(highest_Rated, x=labels, y=counts ,title="Number of ratings of highest rated i phones")
figure.show()


# In[30]:


iphones


# In[9]:


iphones = highest_Rated["Product Name"].value_counts()
labels = iphones.index
counts = highest_Rated["Number Of Reviews"]
figure = px.bar(highest_Rated, x=labels, y=counts ,title="Number of reviews of highest rated i phones")
figure.show()


# In[10]:


figure = px.scatter(data_frame = data, x= "Number Of Ratings", y= "Sale Price", size="Discount Percentage", trendline= "ols", 
                    title="Relationship between sale price and number of rating")
figure.show()


# In[11]:


figure = px.scatter(data_frame = data, x= "Number Of Ratings", y= "Discount Percentage", size="Sale Price", trendline= "ols", 
                    title="Relationship between Discount percentage and number of rating")
figure.show()


# In[ ]:




