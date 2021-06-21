#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd


# In[95]:


driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')

url = 'https://www.zoominfo.com/companies-search/location-macedonia-industry-healthcare'
driver.get(url)


# In[98]:


a = []

site = driver.find_elements_by_css_selector('a.link.amplitudeElement')
#for i in site:
    #print(i.text)
    #a.append(i.text)

for i in range(len(site)):
    if i%2 == 0:
        a.append(site[i].text)



df = pd.DataFrame(a)

df


# In[99]:


df.to_csv(r'E:\SkyQuest\country\N\North Macedonia\2.csv')


# In[ ]:





# In[ ]:




