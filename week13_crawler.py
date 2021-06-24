#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
print(os.getcwd())


# In[3]:


import requests

req = requests.get('https://towardsdatascience.com/')


# In[4]:


req


# In[5]:


webpage = req.text


# In[8]:


print(webpage)


# In[6]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage, 'html.parser')


# In[53]:





# In[7]:


print(soup.prettify())


# In[9]:


heading1 = soup.find_all('h1')


# In[54]:


heading1[0].get_text()


# In[72]:


h=heading1[0].contents[0].get('href')
h


# In[77]:


head = 'https://towardsdatascience.com/'
data = {"title":[], "link":[]}
for h1 in heading1:
    data['title'].append(h1.get_text())
    data['link'].append(head+h1.contents[0].get('href'))
    


# In[78]:


import pandas as pd
df = pd.DataFrame(data)


# In[79]:


df


# In[80]:


df.to_csv("towards_ds.csv")


# In[11]:


heading2 = soup.find_all('h2')


# In[21]:


type(heading2)


# In[ ]:


heading2 = soup.find('h2', attrs={"href":False})

