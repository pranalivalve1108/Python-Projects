#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


df = pd.read_csv("Your Career Aspirations of GenZ.csv")


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.head()


# # Analysis of country

# In[7]:


country = df["Your Current Country."].value_counts()


# In[8]:


country


# In[ ]:





# In[9]:


country = df["Your Current Country."].value_counts()
label = country.index
counts = country.values
colors =['red','lightgreen']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Current Country")
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30, marker = dict(colors = colors, 
                                                                    line=dict(color='black', width = 3)))
fig.show()


# # factors influencing career aspirations

# In[10]:


df.head()


# In[14]:


a = df["Which of the below factors influence the most about your career aspirations ?"].value_counts()
label = a.index
counts = a.values
colors =['gold','lightgreen']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Factors influencing career aspirations")
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30, marker = dict(colors = colors, 
                                                                    line=dict(color='black', width = 3)))
fig.show()


# In[19]:


b = "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
b =df[b].value_counts()


# In[29]:


b


# # How many pursue higher education outside india with their investment?

# In[28]:


c = df["Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."].value_counts()
label = c.index
counts = c.values
colors =['gold','lightgreen','red']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "How many pursue higher education outside india with their investment?")
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30, marker = dict(colors = colors, 
                                                                    line=dict(color='black', width = 3)))
fig.show()


# In[30]:


df.head()


# In[35]:


d = df["How likely is that you will work for one employer for 3 years or more ?"].value_counts()
label = d.index
counts = d.values
colors = ['lightblue','lightgreen','gold']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Work for one employer for 3 years or more")
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 20,
                 marker = dict(colors = colors, line = dict(color = "red", width = 2)))
fig.show()


# # What is the most preferred working environment for you.

# In[42]:


abc = df["What is the most preferred working environment for you."].value_counts()
label = abc.index
counts = abc.values
color = ['aqua','pink','purple']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Most preferred working environment for you.")
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 20, marker = dict(colors = color, 
                                                                line = dict(color = "black", width = 3)))
fig.show()


# In[ ]:




