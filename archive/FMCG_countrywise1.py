#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
url = 'https://en.wikipedia.org/wiki/Category:Lists_of_companies_by_country'
driver.get(url)


# In[5]:


company = []


# In[6]:


name1 = driver.find_elements_by_css_selector('a')
for i in name1:
    print(i.text)
    company.append(i.text)
links = [i.get_attribute('href') for i in name1]


# In[7]:


company.index('Lists of companies of Afghanistan')


# In[8]:


company.index('List of companies of Zimbabwe')


# In[21]:


links=[]


# In[22]:


for i in range(43,390):
    #c.append(company[i])
    company[i]=company[i].replace(" ","_")
    company[i]=company[i].replace("Lists","List")
    links.append('https://en.wikipedia.org/wiki/'+company[i])


# In[23]:


links


# In[24]:


links[0][30:]


# In[94]:


list1=[]


# In[72]:


import time


# In[905]:



driver.get(links[k])

company = []
name1 = driver.find_elements_by_css_selector('td')
for i in name1:
    #print(i.text)
    company.append(i.text)
    

c=[]
for i in range(len(company)):
    if(company[i]=='Consumer goods'):
        c.append(company[i-1])
    

list1=[]
list1.append(links[k][30:])
for i in c:
    list1.append(i)
    df= pd.DataFrame(c)
    #s=links[45][30:]
    #df.to_csv(s.csv)

df= pd.DataFrame(list1)

df

links[k][30:]


# In[893]:


df.to_csv(r'E:\SkyQuest\Stock_exchange\FMCG country wise\cg\List_of_companies_of_Åland.csv')


# In[903]:


k= k+1


# In[904]:


k


# In[ ]:





# In[ ]:




