#!/usr/bin/env python
# coding: utf-8

# In[408]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')

#url = 'https://en.wikipedia.org/wiki/List_of_companies_of_Angola'
driver.get('https://www.lookup.pk/dynamic/search.aspx?searchtype=kl&k=fmcg&l=pakistan')


# In[409]:


company = []


# In[410]:


name1 = driver.find_elements_by_css_selector('h2')
for i in name1:
    print(i.text)
    company.append(i.text)


# In[412]:


len(company)


# In[413]:


company


# In[414]:


df= pd.DataFrame(company)

df


# In[415]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\FMCG country wise\asia\Pakistan1.csv')

driver.close()


# In[ ]:




