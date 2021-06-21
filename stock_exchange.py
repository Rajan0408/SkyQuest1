#!/usr/bin/env python
# coding: utf-8

# In[58]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
url = 'https://topforeignstocks.com/stock-lists/the-list-of-listed-finnish-companies-on-the-nasdaq-omx-helsinki/'
driver.get(url)


# In[62]:


company = []
name1 = driver.find_elements_by_css_selector('td.column-2')
for i in name1:
    print(i.text)
    company.append(i.text)


# In[63]:


company.index('Amer Sports Oyj')


# In[64]:


company.index('Suominen')


# In[65]:


df = pd.DataFrame(company[16:30])
df


# In[66]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\FMCG\New folder\Helsinki Stock Exchange.csv')


# In[ ]:




