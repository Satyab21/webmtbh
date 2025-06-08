#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Install & Import Packages ###

# pip install -upgrade setuptools --user
# pip install atlassian-python-api --user

from atlassian import Confluence
import pandas as pd

from pandas import DataFrame as df

import datetime
from datetime import datetime, timezone, timedelta
from pytz import timezone as tzpy


# In[2]:


# ### Variables: Satya ###
# url_base = 'satyabhambhani21'
# email_admin = 'satyabhambhani21@gmail.com'
# apikey = 'ReaaJSjQCsZUYTbPkhE13EA5'


# In[3]:


### Variables: Neha ###
url_base = 'satyabhambhani21'
email_admin = 'satyabhambhani21@gmail.com'
apikey = 'ReaaJSjQCsZUYTbPkhE13EA5'


# In[4]:


### Admin ###
url_server = f'https://{url_base}.atlassian.net/wiki'

# my team members
email_sdsu = 'sbhambhani4651@sdsu.edu'
email_yahoo = 'satyab21@yahoo.in'


# In[5]:


### Instantiate ###
confluence = Confluence(
    url=url_server, 
    username=email_admin, 
    password=apikey)


# ## Get Data

# In[6]:


### Get Data ###

spaces = confluence.get_all_spaces()
df_spaces = df(spaces['results'], columns=['id', 'key', 'name', 'status', 'type'])
df_spaces = df_spaces[df_spaces['type']=='global']
display(df_spaces)

list_space_page_details = []
for idx_s, row_s in df_spaces.iterrows():
    
    space_key = row_s['key']
    space_id = row_s['id']
    space_name = row_s['name']
    
    df_get_all_pages = df(confluence.get_all_pages_from_space(space=space_key))
#     display(df_get_all_pages)
    
    
    for idx_p, rp in df_get_all_pages.iterrows(): # row-p
        page_id = rp['id']
        page_title = rp['title']
        page_status = rp['status']
        
        history = confluence.history(page_id)        
        lastUpdated = history['lastUpdated']            
        lastUpdated_by = lastUpdated['by']
        createdBy = history['createdBy']
        
        lastUpdated_by_displayName = lastUpdated_by['displayName']
        lastUpdated_by_email = lastUpdated_by['email']
        lastUpdated_by_accountId = lastUpdated_by['accountId'] 
        
        lastUpdated_when = lastUpdated['when']
        lastUpdated_friendlyWhen = lastUpdated['friendlyWhen']
                
        createdBy_email = createdBy['email']
        createdBy_displayName = createdBy['displayName']
        
        createdDate = history['createdDate']
        
        dict_page = {
            'space_id' : space_id,
            'space_key' : space_key,
            'space_name' : space_name,
            
            'page_id' : page_id,
            'page_title' : page_title,
            'page_status' : page_status,
            
            'lastUpdated_by_displayName': lastUpdated_by_displayName,
            'lastUpdated_by_accountId' : lastUpdated_by_accountId,
            'lastUpdated_by_email' : lastUpdated_by_email,
            
            'lastUpdated_when' : lastUpdated_when,
            'lastUpdated_friendlyWhen' : lastUpdated_friendlyWhen,
            
            'createdBy_email' : createdBy_email,
            'createdBy_displayName' : createdBy_displayName,
            'createdDate' : createdDate       
        }
        list_space_page_details.append(dict_page)
        
# df_cf = (df(list_space_page_details))   
df_cf_col = [
    'space_id',
    'space_name',

    'page_title',

    'lastUpdated_friendlyWhen',
    'lastUpdated_by_displayName',
    'lastUpdated_by_email',
    'lastUpdated_when',
    'lastUpdated_by_accountId',
    
    'createdDate',
    'createdBy_displayName',
    'createdBy_email',
    
    'page_id',
    'space_key',
    'page_status'
]

df_cf = df(list_space_page_details, columns=df_cf_col)
display(df_cf)


# In[7]:


# # timezone

# ts = df_cf['lastUpdated_when'][0]
# (ts)

# utc = datetime.fromisoformat(ts[:-1]).astimezone(timezone.utc)
# pst = (utc.replace(tzinfo=timezone.utc).astimezone(tz=None))
# # pst = (utc.replace(tzinfo=timezone.utc).astimezone(timezone('US/Pacific')))

# pst

# pst = pst.astimezone(tzpy('US/Pacific'))

