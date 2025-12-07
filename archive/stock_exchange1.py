#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')


# In[2]:


ur = []
j=20;
for i in range(128):
    ur.append('https://www.cse-india.com/listi/company/'+str(j))
    j = j + 20


# In[3]:


ur


# In[5]:


company = []


# In[6]:


for url in ur:
    
    driver.get(url)



    name1 = driver.find_elements_by_css_selector('td.tableRow1')
    for i in name1:
        print(i.text)
        company.append(i.text)


# In[12]:


len(company)


# In[11]:


company[:10]


# In[10]:


for i in company:
    company.remove("")


# In[ ]:





# In[242]:


company.index('3M India LTD')


# In[243]:


company.index('A T N INTERNATIONAL LTD')


# In[244]:


company.index('A T N INTERNATIONAL LTD')


# In[72]:


company.index('American Pacific Mining Corp.')


# In[13]:


df= pd.DataFrame(company)


# In[14]:


df.head()


# In[15]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\New folder\New folder\asian\CSE(all).csv')


# In[ ]:





# In[ ]:




