#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
url = 'https://en.wikipedia.org/wiki/Category:Food_and_drink_companies_of_Japan'
driver.get(url)


# In[2]:


company = []


# In[3]:


name1 = driver.find_elements_by_css_selector('li')
for i in name1:
    print(i.text)
    company.append(i.text)


# In[5]:


len(company)


# In[7]:


company.index('Fujimitsu Corporation')


# In[8]:


company.index('Yamazaki Baking')


# In[9]:


df= pd.DataFrame(company[11:49])


# In[10]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\FMCG country wise\New folder\Japan.csv')


# In[ ]:




