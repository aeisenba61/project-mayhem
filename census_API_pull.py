
# coding: utf-8

# In[1]:


# Modules
import pandas as pd
import requests
from census import Census
from us import states


# In[2]:


# Census API Key from class and target year for our data
c = Census('85ac64b6b5a9c0901b00329d1ef41f0c53ccfc98', year=2014)


# In[6]:


# Make list of target locations using census format
locations = ['003', '510', '013', '550', '041', '059', '650', '087',
             '107', '700', '710', '153', '760', '177', '179', '810']

# Create empty list to store the returned data dictionaries from each location
census_data = []


# In[7]:


# Loop API calls for each of the target locations
for loc in locations:
    loc_data = c.acs5.get(('NAME', 'B19013_001E', 'B01003_001E', 'B01002_001E'),
                             {'for': 'county :' + loc , 'in': 'state : 51'})
    
    # Append the consolidated data list with the individual location data
    census_data.append(loc_data)
    
print(census_data)   

