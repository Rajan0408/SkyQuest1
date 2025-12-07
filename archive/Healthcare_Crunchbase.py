#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(r'E:\chrome\chromedriver.exe')
url = 'https://www.crunchbase.com/organization/151-products'
driver.get(url)


# In[3]:


Organization_Name = []
name1 = driver.find_element_by_class_name('profile-name')
#print(name1.text)
Organization_Name.append(name1.text)

Organization_Name_URL = []
name1 = driver.find_element_by_css_selector('a.mat-tab-link.mat-focus-indicator.mat-tab-label-active.ng-star-inserted')
name1.get_attribute('href')
Organization_Name_URL.append(name1.get_attribute('href'))

Description= []
desc1 = driver.find_element_by_css_selector('span.description')
Description.append(desc1.text)

Date = []
date1 = driver.find_elements_by_css_selector('span.component--field-formatter.field-type-date_precision.ng-star-inserted')
if len(date1):
    Date.append(date1[0].text)

funding1 = driver.find_elements_by_css_selector('span.component--field-formatter.field-type-money.ng-star-inserted')
Total_Funding_Amount =[]
if len(funding1):
    Total_Funding_Amount.append(funding1[0].text)
    
site1 = driver.find_element_by_css_selector('a.component--field-formatter.layout-row.layout-align-start-end.link-accent.ng-star-inserted')
Website = []
Website.append(site1.text)

ul = driver.find_element_by_css_selector('a.component--field-formatter.field-type-integer.link-accent.ng-star-inserted')
cb_rank =[]
cb_rank.append(ul.text)

ul = driver.find_element_by_css_selector('span.component--field-formatter.field-type-enum.ng-star-inserted')
ipo_status =[]
ipo_status.append(ul.text)

ul = driver.find_element_by_css_selector('a.component--field-formatter.field-type-enum.link-accent.ng-star-inserted')
Number_of_Employees = []
Number_of_Employees.append(ul.text)

ul = driver.find_element_by_css_selector('span.component--field-formatter.field-type-identifier-multi')
Headquarters_Location= []
Headquarters_Location.append(ul.text)

elem = driver.find_elements_by_css_selector('li.ng-star-inserted')

import re

Facebook=[]
LinkedIn = []
Twitter = []
ul = driver.find_elements_by_css_selector('a.component--field-formatter.layout-row.layout-align-start-end.icon-only.link-primary.ng-star-inserted')

for i in range(len(ul)):
    print(ul[i].get_attribute('href'),i)
    if(re.findall("facebook", ul[i].get_attribute('href'))):
        Facebook.append(ul[i].get_attribute('href'))
    if(re.findall("linkedin", ul[i].get_attribute('href'))):
        LinkedIn.append(ul[i].get_attribute('href'))
    if(re.findall("twitter", ul[i].get_attribute('href'))):
        Twitter.append(ul[i].get_attribute('href'))

Industries=[]
Headquarters_Regions=[]
Founders = []
Status =[]
Funding_Type =[]
Also_Known_As = []
Legal_Name  =[]
Related_Hubs=[]
Stock_Symbol  =[]
Company_Type =[]
Exits=[]
Estimated_Revenue_Range=[]
Founded_Date=[]
Contact_Email=[]
Phone_Number=[]
for i in range(len(elem)):
    for word in range(len(elem[i].text.split())):
        if elem[i].text.split()[word] == 'Industries':
            Industries.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Range':
            Estimated_Revenue_Range.append(", ".join(elem[i].text.split()[3:]))
        if elem[i].text.split()[word] == 'Regions':
            Headquarters_Regions.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Founders':
            Founders.append(" ".join(elem[i].text.split()[1:]))
        if elem[i].text.split()[word] == 'Status':
            Status.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Type':
            if elem[i].text.split()[word-1] == 'Funding':
                Funding_Type.append(", ".join(elem[i].text.split()[3:]))
            else:
                Company_Type.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'As':
            Also_Known_As.append(", ".join(elem[i].text.split()[3:]))
        if elem[i].text.split()[word] == 'Name':
            Legal_Name.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Hubs':
            Related_Hubs.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Symbol':
            Stock_Symbol.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Exits':
            Exits.append(", ".join(elem[i].text.split()[3:]))
        if elem[i].text.split()[word] == 'Date':
            Founded_Date.append(" ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Email':
            Contact_Email.append(", ".join(elem[i].text.split()[2:]))
        if elem[i].text.split()[word] == 'Number':
            if elem[i].text.split()[word-1] == 'Phone':
                Phone_Number.append(" ".join(elem[i].text.split()[2:]))

descc = driver.find_elements_by_css_selector('button.mat-focus-indicator.mat-button.mat-button-base.mat-accent.ng-star-inserted')
if len(descc):
    descc[0].click()
time.sleep(1)

ul = driver.find_elements_by_css_selector('div.expanded')
Full_Description =[]
if len(ul):
    Full_Description.append(ul[0].text)

sub_org = []
date1 = driver.find_elements_by_css_selector('a.component--field-formatter.field-type-integer.link-accent.ng-star-inserted')
sub_org.append(date1[len(date1)-1].text)



#FINANCIAL
next1 = driver.find_elements_by_css_selector('a.mat-tab-link.mat-focus-indicator.ng-star-inserted')
Number_of_Lead_Investments=[]
Stock_Symbol = []
Number_of_Exits = []
Total_Funding_Amount = []
Number_of_Funding_Rounds = []
Number_of_Investments = []
    
Number_of_Current_Team_Members=[]
Number_of_Board_Members = []
    
Total_Products_Active=[]
Downloads_Last_30_Days = []
Active_Tech_Count = []
Monthly_Visits = []
Monthly_Visits_Growth = []
    
Number_of_Articles = []
events = []

Number_of_Acquisitions =[]
Number_of_Lead_Investors =[]
Number_of_Investors =[]
Number_of_Diversity_Investments =[]

for k in next1:
    if k.text == 'Financials':
        k.click()
        time.sleep(1)
        elem = driver.find_elements_by_css_selector('div.spacer.ng-star-inserted')

        for i in range(len(elem)):
            for word in range(len(elem[i].text.split())):
                if elem[i].text.split()[word] == 'Investments':
                    if elem[i].text.split()[word-1] == 'Lead':
                        Number_of_Lead_Investments.append(elem[i].text.split()[word+1])
                    else:
                        Number_of_Investments.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Symbol':
                    Stock_Symbol.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Exits':
                    Number_of_Exits.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Rounds':
                    Number_of_Funding_Rounds.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Amount':
                    Total_Funding_Amount.append(elem[i].text.split()[word+1])

        elem = driver.find_elements_by_css_selector('big-values-card.ng-star-inserted')




        for i in range(len(elem)):
                    for word in range(len(elem[i].text.split())):
                        if elem[i].text.split()[word] == 'Investors':
                            if elem[i].text.split()[word-1] == 'Lead':
                                Number_of_Lead_Investors.append(elem[i].text.split()[word+1])
                            else:
                                Number_of_Investors.append(elem[i].text.split()[word+1])
                        if elem[i].text.split()[word] == 'Investments':
                            if elem[i].text.split()[word-1] == 'Diversity':
                                Number_of_Diversity_Investments.append(elem[i].text.split()[word+1])
                        if elem[i].text.split()[word] == 'Acquisitions':
                            Number_of_Acquisitions.append(elem[i].text.split()[word+1])

#PEOPLE

    if k.text == 'People':
        k.click()
        time.sleep(1)
        elem = driver.find_elements_by_css_selector('div.spacer.ng-star-inserted')

        Number_of_Current_Team_Members=[]
        Number_of_Board_Members = []
        for i in range(len(elem)):
            for word in range(len(elem[i].text.split())):
                if elem[i].text.split()[word] == 'Members':
                    if elem[i].text.split()[word-1] == 'Team':
                        Number_of_Current_Team_Members.append(elem[i].text.split()[word+1])
                    else:
                        Number_of_Board_Members.append(elem[i].text.split()[word+3])

#TECHNOLOGY
    if k.text == 'Technology':
        k.click()
        time.sleep(1)

        elem = driver.find_elements_by_css_selector('div.spacer.ng-star-inserted')


        for i in range(len(elem)):
            for word in range(len(elem[i].text.split())):
                if elem[i].text.split()[word] == 'Active':
                    Total_Products_Active.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Days':
                    Downloads_Last_30_Days.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Count':
                    Active_Tech_Count.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Visits':
                    Monthly_Visits.append(elem[i].text.split()[word+1])
                if elem[i].text.split()[word] == 'Growth':
                    Monthly_Visits_Growth.append(elem[i].text.split()[word+1])

#news

    if k.text == 'Signals & News':
        k.click()
        time.sleep(1)

        elem = driver.find_elements_by_css_selector('a.component--field-formatter.field-type-integer.link-accent.ng-star-inserted')

        if len(elem):
            if len(elem) == 1:
                Number_of_Articles.append(elem[0].text)
            if len(elem) == 2:
                Number_of_Articles.append(elem[0].text)
                events.append(elem[1].text)

final = [Organization_Name,Organization_Name_URL,Description,
Founded_Date,
Total_Funding_Amount,
Website,
cb_rank,
ipo_status,
Number_of_Employees,
Headquarters_Location,Facebook,
LinkedIn,
Twitter,Industries,
Headquarters_Regions,
Founders,
Status,
Funding_Type,
Also_Known_As,
Legal_Name,
Related_Hubs,
Stock_Symbol,
Company_Type,
Exits,
Estimated_Revenue_Range,
Contact_Email,
Phone_Number,
Number_of_Lead_Investments,
Stock_Symbol,
Number_of_Exits,
Total_Funding_Amount,
Number_of_Funding_Rounds,
Number_of_Investments,
    
Number_of_Current_Team_Members,
Number_of_Board_Members,
    
Total_Products_Active,
Downloads_Last_30_Days,
Active_Tech_Count,
Monthly_Visits,
Monthly_Visits_Growth,
    
Number_of_Articles,events,
Number_of_Acquisitions,
Number_of_Lead_Investors,
Number_of_Investors,
Number_of_Diversity_Investments]

for i in final:
    if not len(i):
        i.append("None")


df = pd.DataFrame(list(zip(final[0],final[1],final[2],final[3],final[4],final[5],final[6],final[7],final[8],final[9],final[10],final[11],final[12],final[13],final[14],final[15],final[16],final[17],final[18],final[19],final[20],final[21],final[22],final[23],final[24],final[25],final[26],final[27],final[28],final[29],final[30],final[31],final[32],final[33],final[34],final[35],final[36],final[37],final[38],final[39],final[40],final[41],final[42],final[43],final[44],final[45])),
columns =['Organization_Name','Organization_Name_URL','Description',
'Founded_Date',
'Total_Funding_Amount',
'Website',
'cb_rank',
'ipo_status',
'Number_of_Employees',
'Headquarters_Location','Facebook',
'LinkedIn',
'Twitter','Industries',
'Headquarters_Regions',
'Founders',
'Status',
'Funding_Type',
'Also_Known_As',
'Legal_Name',
'Related_Hubs',
'Stock_Symbol',
'Company_Type',
'Exits',
'Estimated_Revenue_Range',
'Contact_Email',
'Phone_Number',
'Number_of_Lead_Investments',
'Stock_Symbol',
'Number_of_Exits',
'Total_Funding_Amount',
'Number_of_Funding_Rounds',
'Number_of_Investments',
    
'Number_of_Current_Team_Members',
'Number_of_Board_Members',
    
'Total_Products_Active',
'Downloads_Last_30_Days',
'Active_Tech_Count',
'Monthly_Visits',
'Monthly_Visits_Growth',
    
'Number_of_Articles','events',
'Number_of_Acquisitions',
'Number_of_Lead_Investors',
'Number_of_Investors',
'Number_of_Diversity_Investments'])


# In[4]:


df


# In[5]:


list1 = pd.read_csv(r'E:\SkyQuest\pest\1.csv',encoding='latin-1')
list1
x = list1.iloc[:,2]


# In[84]:


l =[17,18,21,22,24,26,34,35,36,37,40,45,47,51,53,71]


# In[88]:


links


# In[87]:


for links in l:
    driver.get(x[links])
    Organization_Name = []
    name1 = driver.find_element_by_class_name('profile-name')
    #print(name1.text)
    Organization_Name.append(name1.text)

    Organization_Name_URL = []
    name1 = driver.find_element_by_css_selector('a.mat-tab-link.mat-focus-indicator.mat-tab-label-active.ng-star-inserted')
    name1.get_attribute('href')
    Organization_Name_URL.append(name1.get_attribute('href'))

    Description= []
    desc1 = driver.find_element_by_css_selector('span.description')
    Description.append(desc1.text)

    Date = []
    date1 = driver.find_elements_by_css_selector('span.component--field-formatter.field-type-date_precision.ng-star-inserted')
    if len(date1):
        Date.append(date1[0].text)

    funding1 = driver.find_elements_by_css_selector('span.component--field-formatter.field-type-money.ng-star-inserted')
    Total_Funding_Amount =[]
    if len(funding1):
        Total_Funding_Amount.append(funding1[0].text)

    site1 = driver.find_elements_by_css_selector('a.component--field-formatter.layout-row.layout-align-start-end.link-accent.ng-star-inserted')
    Website = []
    if len(site1):
        Website.append(site1[0].text)

    ul = driver.find_element_by_css_selector('a.component--field-formatter.field-type-integer.link-accent.ng-star-inserted')
    cb_rank =[]
    cb_rank.append(ul.text)

    ul = driver.find_element_by_css_selector('span.component--field-formatter.field-type-enum.ng-star-inserted')
    ipo_status =[]
    ipo_status.append(ul.text)

    ul = driver.find_elements_by_css_selector('a.component--field-formatter.field-type-enum.link-accent.ng-star-inserted')
    Number_of_Employees = []
    if len(ul):
        Number_of_Employees.append(ul[0].text)

    ul = driver.find_element_by_css_selector('span.component--field-formatter.field-type-identifier-multi')
    Headquarters_Location= []
    Headquarters_Location.append(ul.text)

    elem = driver.find_elements_by_css_selector('li.ng-star-inserted')

    import re

    Facebook=[]
    LinkedIn = []
    Twitter = []
    ul = driver.find_elements_by_css_selector('a.component--field-formatter.layout-row.layout-align-start-end.icon-only.link-primary.ng-star-inserted')

    for i in range(len(ul)):
       # print(ul[i].get_attribute('href'),i)
        if(re.findall("facebook", ul[i].get_attribute('href'))):
            Facebook.append(ul[i].get_attribute('href'))
        if(re.findall("linkedin", ul[i].get_attribute('href'))):
            LinkedIn.append(ul[i].get_attribute('href'))
        if(re.findall("twitter", ul[i].get_attribute('href'))):
            Twitter.append(ul[i].get_attribute('href'))

    Industries=[]
    Headquarters_Regions=[]
    Founders = []
    Status =[]
    Funding_Type =[]
    Also_Known_As = []
    Legal_Name  =[]
    Related_Hubs=[]
    Stock_Symbol  =[]
    Company_Type =[]
    Exits=[]
    Estimated_Revenue_Range=[]
    Founded_Date=[]
    Contact_Email=[]
    Phone_Number=[]
    for i in range(len(elem)):
        for word in range(len(elem[i].text.split())):
            if elem[i].text.split()[word] == 'Industries':
                Industries.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Range':
                Estimated_Revenue_Range.append(", ".join(elem[i].text.split()[3:]))
            if elem[i].text.split()[word] == 'Regions':
                Headquarters_Regions.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Founders':
                Founders.append(" ".join(elem[i].text.split()[1:]))
            if elem[i].text.split()[word] == 'Status':
                Status.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Type':
                if elem[i].text.split()[word-1] == 'Funding':
                    Funding_Type.append(", ".join(elem[i].text.split()[3:]))
                else:
                    Company_Type.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'As':
                Also_Known_As.append(", ".join(elem[i].text.split()[3:]))
            if elem[i].text.split()[word] == 'Name':
                Legal_Name.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Hubs':
                Related_Hubs.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Symbol':
                Stock_Symbol.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Exits':
                Exits.append(", ".join(elem[i].text.split()[3:]))
            if elem[i].text.split()[word] == 'Date':
                Founded_Date.append(" ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Email':
                Contact_Email.append(", ".join(elem[i].text.split()[2:]))
            if elem[i].text.split()[word] == 'Number':
                if elem[i].text.split()[word-1] == 'Phone':
                    Phone_Number.append(" ".join(elem[i].text.split()[2:]))

    descc = driver.find_elements_by_css_selector('button.mat-focus-indicator.mat-button.mat-button-base.mat-accent.ng-star-inserted')
    if len(descc):
        descc[0].click()
    time.sleep(1)

    ul = driver.find_elements_by_css_selector('div.expanded')
    Full_Description =[]
    if len(ul):
        Full_Description.append(ul[0].text)

    sub_org = []
    date1 = driver.find_elements_by_css_selector('a.component--field-formatter.field-type-integer.link-accent.ng-star-inserted')
    sub_org.append(date1[len(date1)-1].text)



    #FINANCIAL
    next1 = driver.find_elements_by_css_selector('a.mat-tab-link.mat-focus-indicator.ng-star-inserted')
    Number_of_Lead_Investments=[]
    Stock_Symbol = []
    Number_of_Exits = []
    Total_Funding_Amount = []
    Number_of_Funding_Rounds = []
    Number_of_Investments = []

    Number_of_Current_Team_Members=[]
    Number_of_Board_Members = []

    Total_Products_Active=[]
    Downloads_Last_30_Days = []
    Active_Tech_Count = []
    Monthly_Visits = []
    Monthly_Visits_Growth = []

    Number_of_Articles = []
    events = []

    Number_of_Acquisitions =[]
    Number_of_Lead_Investors =[]
    Number_of_Investors =[]
    Number_of_Diversity_Investments =[]

    for k in next1:
        if k.text == 'Financials':
            k.click()
            time.sleep(1)
            elem = driver.find_elements_by_css_selector('div.spacer.ng-star-inserted')

            for i in range(len(elem)):
                for word in range(len(elem[i].text.split())):
                    if elem[i].text.split()[word] == 'Investments':
                        if elem[i].text.split()[word-1] == 'Lead':
                            Number_of_Lead_Investments.append(elem[i].text.split()[word+1])
                        else:
                            Number_of_Investments.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Symbol':
                        Stock_Symbol.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Exits':
                        Number_of_Exits.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Rounds':
                        Number_of_Funding_Rounds.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Amount':
                        Total_Funding_Amount.append(elem[i].text.split()[word+1])

            elem = driver.find_elements_by_css_selector('big-values-card.ng-star-inserted')




            for i in range(len(elem)):
                        for word in range(len(elem[i].text.split())):
                            if elem[i].text.split()[word] == 'Investors':
                                if elem[i].text.split()[word-1] == 'Lead':
                                    Number_of_Lead_Investors.append(elem[i].text.split()[word+1])
                                else:
                                    Number_of_Investors.append(elem[i].text.split()[word+1])
                            if elem[i].text.split()[word] == 'Investments':
                                if elem[i].text.split()[word-1] == 'Diversity':
                                    Number_of_Diversity_Investments.append(elem[i].text.split()[word+1])
                            if elem[i].text.split()[word] == 'Acquisitions':
                                Number_of_Acquisitions.append(elem[i].text.split()[word+1])

    #PEOPLE

        if k.text == 'People':
            k.click()
            time.sleep(1)
            elem = driver.find_elements_by_css_selector('div.spacer.ng-star-inserted')

            Number_of_Current_Team_Members=[]
            Number_of_Board_Members = []
            for i in range(len(elem)):
                for word in range(len(elem[i].text.split())):
                    if elem[i].text.split()[word] == 'Members':
                        if elem[i].text.split()[word-1] == 'Team':
                            Number_of_Current_Team_Members.append(elem[i].text.split()[word+1])
                        else:
                            Number_of_Board_Members.append(elem[i].text.split()[word+3])

    #TECHNOLOGY
        if k.text == 'Technology':
            k.click()
            time.sleep(1)

            elem = driver.find_elements_by_css_selector('div.spacer.ng-star-inserted')


            for i in range(len(elem)):
                for word in range(len(elem[i].text.split())):
                    if elem[i].text.split()[word] == 'Active':
                        Total_Products_Active.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Days':
                        Downloads_Last_30_Days.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Count':
                        Active_Tech_Count.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Visits':
                        Monthly_Visits.append(elem[i].text.split()[word+1])
                    if elem[i].text.split()[word] == 'Growth':
                        Monthly_Visits_Growth.append(elem[i].text.split()[word+1])

    #news

        if k.text == 'Signals & News':
            k.click()
            time.sleep(1)

            elem = driver.find_elements_by_css_selector('a.component--field-formatter.field-type-integer.link-accent.ng-star-inserted')

            if len(elem):
                if len(elem) == 1:
                    Number_of_Articles.append(elem[0].text)
                if len(elem) == 2:
                    Number_of_Articles.append(elem[0].text)
                    events.append(elem[1].text)

    final = [Organization_Name,Organization_Name_URL,Description,
    Founded_Date,
    Total_Funding_Amount,
    Website,
    cb_rank,
    ipo_status,
    Number_of_Employees,
    Headquarters_Location,Facebook,
    LinkedIn,
    Twitter,Industries,
    Headquarters_Regions,
    Founders,
    Status,
    Funding_Type,
    Also_Known_As,
    Legal_Name,
    Related_Hubs,
    Stock_Symbol,
    Company_Type,
    Exits,
    Estimated_Revenue_Range,
    Contact_Email,
    Phone_Number,
    Number_of_Lead_Investments,
    Stock_Symbol,
    Number_of_Exits,
    Total_Funding_Amount,
    Number_of_Funding_Rounds,
    Number_of_Investments,

    Number_of_Current_Team_Members,
    Number_of_Board_Members,

    Total_Products_Active,
    Downloads_Last_30_Days,
    Active_Tech_Count,
    Monthly_Visits,
    Monthly_Visits_Growth,

    Number_of_Articles,events,
    Number_of_Acquisitions,
    Number_of_Lead_Investors,
    Number_of_Investors,
    Number_of_Diversity_Investments]

    for i in final:
        if not len(i):
            i.append("None")


    df1 = pd.DataFrame(list(zip(final[0],final[1],final[2],final[3],final[4],final[5],final[6],final[7],final[8],final[9],final[10],final[11],final[12],final[13],final[14],final[15],final[16],final[17],final[18],final[19],final[20],final[21],final[22],final[23],final[24],final[25],final[26],final[27],final[28],final[29],final[30],final[31],final[32],final[33],final[34],final[35],final[36],final[37],final[38],final[39],final[40],final[41],final[42],final[43],final[44],final[45])),
    columns =['Organization_Name','Organization_Name_URL','Description',
    'Founded_Date',
    'Total_Funding_Amount',
    'Website',
    'cb_rank',
    'ipo_status',
    'Number_of_Employees',
    'Headquarters_Location','Facebook',
    'LinkedIn',
    'Twitter','Industries',
    'Headquarters_Regions',
    'Founders',
    'Status',
    'Funding_Type',
    'Also_Known_As',
    'Legal_Name',
    'Related_Hubs',
    'Stock_Symbol',
    'Company_Type',
    'Exits',
    'Estimated_Revenue_Range',
    'Contact_Email',
    'Phone_Number',
    'Number_of_Lead_Investments',
    'Stock_Symbol',
    'Number_of_Exits',
    'Total_Funding_Amount',
    'Number_of_Funding_Rounds',
    'Number_of_Investments',

    'Number_of_Current_Team_Members',
    'Number_of_Board_Members',

    'Total_Products_Active',
    'Downloads_Last_30_Days',
    'Active_Tech_Count',
    'Monthly_Visits',
    'Monthly_Visits_Growth',

    'Number_of_Articles','events',
    'Number_of_Acquisitions',
    'Number_of_Lead_Investors',
    'Number_of_Investors',
    'Number_of_Diversity_Investments'])

    df = df.append(df1)
    print(links)


# In[89]:


df


# In[90]:


df.to_csv(r'E:\SkyQuest\crunchbase_scraping\final2.csv')


# In[ ]:




