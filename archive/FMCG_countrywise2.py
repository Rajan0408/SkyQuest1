#!/usr/bin/env python
# coding: utf-8

# In[76]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
url = 'https://en.wikipedia.org/wiki/List_of_companies_of_China'
driver.get(url)


# In[77]:


company = []


# In[79]:


name1 = driver.find_elements_by_css_selector('td')
for i in name1:
    print(i.text)
    company.append(i.text)


# In[68]:


len(company)


# In[41]:


for i in company:
    company.remove("Share it on Social Media")


# In[ ]:





# In[53]:


company.index('Unilever')


# In[54]:


company.index('Kraft Heinz Company')


# In[244]:


company.index('A T N INTERNATIONAL LTD')


# In[72]:


company.index('American Pacific Mining Corp.')


# In[69]:


df= pd.DataFrame(company)


# In[70]:


df


# In[71]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\FMCG country wise\New folder\United Kingdom3.csv')


# In[ ]:





# In[ ]:




