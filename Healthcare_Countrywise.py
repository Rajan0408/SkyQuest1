#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd


# In[18]:


driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')

url = 'https://www.business1.com/medical-device-companies/togo'
driver.get(url)


# In[21]:


a = []

site = driver.find_elements_by_css_selector('h3')
for i in site:
    print(i.text)
    a.append(i.text)

a

df = pd.DataFrame(a)

df


# In[20]:


df.to_csv(r'E:\SkyQuest\country\T\Togo\1.csv')


# In[ ]:





# In[ ]:




