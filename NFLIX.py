#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime 


# In[6]:


df = pd.read_csv("NFLX.csv")


# In[7]:


df


# In[8]:


df.head()


# In[9]:


sns.set(rc={'figure.figsize' :(10,5)})


# # date column as index

# In[10]:


df['Date'] = pd.to_datetime(df['Date'])
df= df.set_index('Date')
df.head()


# # Volume of Stock Traded

# In[11]:


sns.lineplot(x=df.index, y=df['Volume'], label='Volume')
plt.title("Volume of stock VS time")


# # Netflix stock price- High, Open, Close

# In[12]:


df.plot(y=['High','Close','Open'],title="Netflix stock price")


# # Netflix stock price- Day, Month, Year wise

# In[13]:


fig, (ax1,ax2,ax3)=plt.subplots(3, figsize = (15,10)) 
df.groupby(df.index.day).mean().plot(y='Volume',ax=ax1,xlabel='Day')
df.groupby(df.index.month).mean().plot(y='Volume',ax=ax2,xlabel='Month')
df.groupby(df.index.year).mean().plot(y='Volume',ax=ax3,xlabel='Year')


# # Top 5 Dates with Highest stock price

# In[14]:


a=df.sort_values(by='High', ascending=False).head(5)
a['High']


# # Top 5 Dates with Lowest stock price

# In[15]:


b=df.sort_values(by='Low', ascending=True).head(5)
b['Low']


# In[19]:


fig,axes=plt.subplots(nrows=1, ncols=2,sharex=True, figsize=(12,5))
fig.suptitle('High & Low values stock per period of time', fontsize=18)
sns.lineplot(ax=axes[0], y=df['High'],x=df.index, color='green')
sns.lineplot(ax=axes[1], y=df['Low'],x=df.index, color='red')


# In[ ]:




