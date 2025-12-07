# Archive – Country-Wise & Stock Exchange Web Scraping Scripts

This folder contains **older, experimental, and country-specific web scraping scripts** developed during large-scale data collection for FMCG, Healthcare, and Stock Exchange companies.  
All scripts use **Selenium + Python** to extract company names from Wikipedia, ZoomInfo, Business1, Lookup.pk, and regional stock exchanges.

These files represent previous iterations, testing logic, and standalone scrapers used during exploratory data gathering.

---

##  Scripts Overview

### **FMCG_countrywise.py**
Scrapes FMCG company names from **Lookup.pk** for Pakistan.
- Opens FMCG search page
- Extracts all `<h2>` tags (company names)
- Saves output to CSV

### **FMCG_countrywise1.py**
Scrapes FMCG companies from **ZoomInfo – New Zealand Consumer Goods**.
- Extracts alternating rows (`a.link.amplitudeElement`)
- Saves list of names to CSV

### **FMCG_countrywise2.py**
Scrapes FMCG companies from **Wikipedia – Food & Drink Companies of Japan**.
- Collects all `<li>` tags
- Filters index range to isolate company list
- Exports cleaned result to CSV

### **stock_exchange.py**
Scrapes company names from **CSE India** (20 results per page sequence).
- Auto-generates 128 URLs
- Extracts company names from `td.tableRow1`
- Removes blanks and saves full company list

### **stock_exchange1.py**
Scrapes **listed Finnish companies** from NASDAQ OMX Helsinki (TopForeignStocks).
- Extracts column values from table
- Saves subset (16–30) to CSV

### **stock_exchange2.py**
Scrapes **Healthcare companies in Macedonia** from ZoomInfo.
- Extracts alternating `<a.link.amplitudeElement>` entries
- Saves final list to CSV

### **stock_exchange3.py**
Scrapes Healthcare companies from **Business1 – Togo**.
- Extracts all `<h3>` tags as company names
- Saves output to CSV

### **stock_exchange4.py**
Scrapes **companies of China** from Wikipedia.
- Extracts all `<td>` elements
- Removes noise
- Saves result to CSV

### **Healthcare_Countrywise.py**
Scrapes list of **company-list pages by country** from Wikipedia.
- Extracts all `<a>` links
- Builds country-specific URLs
- Prepares list for further scraping

### **Healthcare_countrywise1.py**
Improved country-wise healthcare scraper.
- Visits each country’s company list page
- Looks for rows labeled *Consumer goods*
- Extracts corresponding companies
- Saves output as country-level CSV

---

## Purpose of This Archive
These scripts are stored here because:

- They represent earlier versions of the final consolidated pipeline  
- They include specialized country-wise and exchange-wise scrapers used for manual dataset creation  
- They serve as reusable reference code for scraping patterns  
- They keep the main project clean while preserving useful logic  

---

##  Notes
- Scripts use **hardcoded paths** (e.g., `E:\SkyQuest\...`)
- Some CSS selectors may be outdated due to website changes  
- Scripts may not run without modification  
- Uses deprecated Selenium methods like `find_elements_by_css_selector`

