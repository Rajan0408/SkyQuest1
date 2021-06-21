#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
url = 'https://en.wikipedia.org/wiki/Category:Lists_of_companies_by_country'
driver.get(url)


# In[2]:


company = []


# In[ ]:


name1 = driver.find_elements_by_css_selector('a')
for i in name1:
    print(i.text)
    company.append(i.text)
#links = [i.get_attribute('href') for i in name1]


# In[5]:


links


# In[6]:


links.index('https://en.wikipedia.org/wiki/Category:Lists_of_companies_of_Afghanistan')


# In[7]:


links.index('https://en.wikipedia.org/wiki/List_of_companies_of_Zimbabwe')


# In[19]:


len(links)


# In[18]:


links = links[43:390]


# In[20]:


links


# In[16]:


links[45][30:]


# In[36]:


s = r'E:\SkyQuest\Stock_exchange\FMCG country wise\New folder\C'+ str(links[45][29:])+str(".csv")


# In[37]:


s


# In[63]:


list1=[]


# In[67]:


import time


# In[74]:


for i in range(len(links)):
    driver.get(links[i])
    time.sleep(5)
    company = []
    name1 = driver.find_elements_by_css_selector('td')
    for i in name1:
        print(i.text)
        company.append(i.text)
    c=[]
    for i in range(len(company)):
        if(company[i]=='Consumer goods'):
            c.append(company[i-1])
    list1.append(links[i])
    list1.append(c)
    df= pd.DataFrame(c)
    #s=links[45][30:]
    #df.to_csv(s.csv)


# In[75]:


list1


# In[ ]:




