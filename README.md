# Healthcare Crunchbase Scraper

This repository contains a Python + Selenium script to scrape detailed company profiles from Crunchbase for a list of healthcare (or any domain) organizations and export the data into a clean CSV file for further analysis. 
---

## What this script does

For each Crunchbase organization URL, the script automatically:

- Opens the company profile using Selenium + Chrome WebDriver
  
- Extracts core company details:
  - Organization name, URL, description
  - Founded date, IPO status, CB rank
  - Funding details (total funding amount, number of rounds, number of exits, etc.)
  - Website & social media links (Facebook, LinkedIn, Twitter)
  - Headquarters location & regions
  - Industries and estimated revenue range
  - Founders, company status, company type, related hubs, stock symbol
  - Contact email & phone number :contentReference[oaicite:1]{index=1}
    
- Navigates through multiple Crunchbase tabs:
  - **Financials** – investments, investors, acquisitions, exits, funding rounds, diversity investments  
  - **People** – team members, board members  
  - **Technology** – active products, downloads, active tech count, monthly visits & growth  
  - **Signals & News** – number of articles and events :contentReference[oaicite:2]{index=2}
    
- Aggregates all fields into a single `pandas` DataFrame and writes the final output to a CSV file (`final2.csv`). :contentReference[oaicite:3]{index=3}  

---

## Input & Output

### Input

1. **CSV of organization links** – The script expects a CSV file containing Crunchbase organization URLs:  
   ```python
   list1 = pd.read_csv(r'E:\SkyQuest\pest\1.csv', encoding='latin-1')
   x = list1.iloc[:, 2]  # uses the 3rd column as the URL column
### Output

The script compiles all scraped company details into a Pandas DataFrame and exports the final results to a CSV file at:

```python
  df.to_csv(r'E:\SkyQuest\crunchbase_scraping\final2.csv')
```

This output CSV contains one row per company with all extracted fields (company profile, funding, people, technology, and news information).

Note: The archive/ folder contains country-wise and stock-exchange scraping scripts used during early dataset collection. These scripts are not part of the main Crunchbase scraper but are preserved for reference and reuse. See archive/ARCHIVE README.md for details.
