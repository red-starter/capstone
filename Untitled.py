#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


# In[9]:


# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2018-01-01'
end_date = '2019-01-01'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader(tickers, 'yahoo', start_date, end_date)


# In[10]:


panel_data.head(10)


# In[ ]:


# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
commodities = x = ["LIT",
"XME",
"PICK",
"REMX",
"COPX",
"BATT"]

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2018-01-01'
end_date = '2019-01-01'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader(commodities, 'yahoo', start_date, end_date)


# In[ ]:


panel_data.head()


# In[ ]:




