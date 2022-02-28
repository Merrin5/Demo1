#!/usr/bin/env python
# coding: utf-8

# # Extracting data from Steam 

# Follow the links below to extract the relevant data from the Steam webpage. 

# ## Initial Setup

# In[ ]:


from bs4 import BeautifulSoup
import requests


# ## Connect to Steam webpage

# In[ ]:


r = requests.get("https://store.steampowered.com/tags/en/Action/")
r.status_code


# In[ ]:


html = r.content


# In[ ]:


soup = BeautifulSoup(html, "lxml")


# In[ ]:





# Extract the following information from the Steam Website:
# - Names of the top games
# - Price
# - Category of game
# - Any further information
# - get the text from the class equal to top-tag
# 
# 
# Store the extracted data in pandas dataFrame and then save as a CSV file.

# ## Answer

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




