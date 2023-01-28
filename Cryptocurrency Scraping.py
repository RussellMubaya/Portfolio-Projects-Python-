#!/usr/bin/env python
# coding: utf-8

# Imports
# 
# 

# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


       


# HTTP Request
#  

# In[5]:


# store website in variable
website = 'https://www.coingecko.com/en'


# In[6]:


# Get request
response = requests.get(website)


# In[7]:


# Status Code
response.status_code


# Soup Object

# In[8]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[ ]:


soup


# Results

# In[10]:


results = soup.find('table',{'class': 'table-scrollable'}).find('tbody').find_all('tr')


# In[11]:


len(results)


# Target necessary data

# In[12]:


# Name
# Price
# 1h Change
# 24h Change
# 7 day change
# 24h Volume
# Market Cap


# Name

# In[13]:


results[0].find('a', {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()


# Price

# In[14]:


results[0].find('td', {'class': 'td-price'}).get_text().strip()


#  1hr Change

# In[15]:


results[0].find('td', {'class': 'td-change1h'}).get_text().strip()


# 24hr Change

# In[16]:


results[0].find('td', {'class': 'td-change24h'}).get_text().strip()


# 7 day change

# In[17]:


results[0].find('td', {'class': 'td-change7d'}).get_text().strip()


# 24hr Volume

# In[18]:


results[0].find('td', {'class': 'td-liquidity_score'}).get_text().strip()


# Market Cap

# In[19]:


results[0].find('td', {'class': 'td-market_cap'}).get_text().strip()


# Put everything together in a for loop

# In[20]:


# empty lists
name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for result in results:
    # name
    try:
        name.append(result.find('a', {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        name.append('n/a')
        
    # price
    try:
        price.append(result.find('td', {'class':'td-price'}).get_text().strip())
    except:
        price.append('n/a')
        
    # change 1h
    try:
        change_1h.append(result.find('td', {'class':'td-change1h'}).get_text().strip())
    except:
        change_1h.append('n/a')
        
    # change 24h
    try:
        change_24h.append(result.find('td', {'class':'td-change24h'}).get_text().strip())
    except:
        change_24h.append('n/a')
        
    # change 7d
    try:
        change_7d.append(result.find('td', {'class':'td-change7d'}).get_text().strip())
    except:
        change_7d.append('n/a')
        
    #volume 24h
    try:
        volume_24h.append(result.find('td', {'class':'td-liquidity_score'}).get_text().strip())
    except:
        volume_24h.append('n/a')
        
    # market cap
    try:
        market_cap.append(result.find('td', {'class':'td-market_cap'}).get_text().strip())
    except:
        market_cap.append('n/a')
    

  
 
                         

    
   


# Create Pandas Dataframe

# In[21]:


crypto_df = pd.DataFrame({'Coin': name, 'Price': price, 'Change_1h': change_1h, 'Change_24h':change_24h, 'Change_7d': change_7d, 'Volume_24h': volume_24h, 'Markt Cap': market_cap})


# In[22]:


#output dataframe
crypto_df


# Output in Excel

# In[23]:


crypto_df.to_excel('single_page_crypto.xlsx', index=False)


# In[ ]:





# Part 2 - Pagination - Get 1000 Results

# In[24]:


# empty lists
name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []


for i in range(1, 11):
    #website
    website = 'https://www.coingecko.com/en?page='+ str(i)
    
    #request to website
    response = requests.get(website)
    
    # soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # storing results in a table
    results = soup.find('table',{'class': 'table-scrollable'}).find('tbody').find_all('tr')
    
    for result in results:
        # name
        try:
            name.append(result.find('a', {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
        except:
            name.append('n/a')

        # price
        try:
            price.append(result.find('td', {'class':'td-price'}).get_text().strip())
        except:
            price.append('n/a')

        # change 1h
        try:
            change_1h.append(result.find('td', {'class':'td-change1h'}).get_text().strip())
        except:
            change_1h.append('n/a')

        # change 24h
        try:
            change_24h.append(result.find('td', {'class':'td-change24h'}).get_text().strip())
        except:
            change_24h.append('n/a')

        # change 7d
        try:
            change_7d.append(result.find('td', {'class':'td-change7d'}).get_text().strip())
        except:
            change_7d.append('n/a')

        #volume 24h
        try:
            volume_24h.append(result.find('td', {'class':'td-liquidity_score'}).get_text().strip())
        except:
            volume_24h.append('n/a')

        # market cap
        try:
            market_cap.append(result.find('td', {'class':'td-market_cap'}).get_text().strip())
        except:
            market_cap.append('n/a')



# In[25]:


crypto_df = pd.DataFrame({'Coin': name, 'Price': price, 'Change_1h': change_1h, 'Change_24h':change_24h, 'Change_7d': change_7d, 'Volume_24h': volume_24h, 'Markt Cap': market_cap})


# In[26]:


crypto_df


# In[27]:


crypto_df.to_excel('multiple_page_crypto.xlsx', index=False)


# In[ ]:




