#!/usr/bin/env python
# coding: utf-8

# In[817]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')

url = 'https://www.zoominfo.com/companies-search/location-new-zealand-industry-consumer-goods'
driver.get(url)


# In[818]:


company = []


# In[824]:


name1 = driver.find_elements_by_css_selector('a.link.amplitudeElement')
for i in range(len(name1)):
    if i%2==0:
        company.append(name1[i].text)
len(company)


# In[825]:


df= pd.DataFrame(company)

df


# In[826]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\FMCG country wise\Oceanic\New Zealand.csv')

driver.close()


# In[ ]:





# In[ ]:





# In[ ]:




