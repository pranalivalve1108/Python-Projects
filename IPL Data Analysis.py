#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("IPL 2022.csv")


# In[3]:


data


# # Number of matches won by each team in IPL 2022

# In[4]:


figure = px.bar(data, x= data["match_winner"], title= "Number of matches in IPL 2022")
figure.show()


# In[ ]:





# In[5]:


figure = px.bar(data, x=data["best_bowling"], title="Best bowler in IPL 2022")
figure.show()


# In[6]:


figure = px.bar(data, x=['player_of_the_match'],
               title="Most player of the match Awards")
figure.show()


# # Top scorer in IPL 2022

# In[7]:


figure = px.bar(data, x=data["top_scorer"], y=data['highscore'], color=data['highscore'],title="Top scorers in IPL 2022")
figure.show()


# In[8]:


data['won_by']=data['won_by'].map({'Wickets':'Chasing',
                                   'Runs':'Defending'})
won_by = data["won_by"].value_counts()
label=won_by.index
counts=won_by.values
colors=['red','lightgreen']
fig=go.Figure(data = [go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Number of matches won by defending or chasing")
fig.update_traces(hoverinfo='label+percent',textinfo="value", textfont_size=30,marker=dict(colors=colors, 
                            line=dict(color='black',width=3)))
figure.show()


# In[ ]:




