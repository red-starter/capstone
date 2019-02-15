#!/usr/bin/env python
# coding: utf-


from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd


tweet_sentiment_df = pd.read_csv('all_days.csv')


tweet_cols = tweet_sentiment_df.columns
start_date = tweet_cols[1]
end_date = tweet_cols[-1]
# get date range
print(start_date,end_date)

# the are main etfs
#"SPDR", S&P 500 ETF 
#"SPY", iShares Core S&P 500 ETF 
#"IVV", Vanguard Total Stock Market ETF 
#"VTI", Vanguard S&P 500 ETF 
#"VOO", PowerShares QQQ 
#"QQQ", iShares Russell 2000 
#"IWM", SPDR Dow Jones Industrial Average 
main_etfs = ["SPY", "IVV", "VTI", "QQQ", "IWM", "DIA"]

# pandas_reader.data.DataReader to load the data. 
panel_data = data.DataReader(main_etfs, 'yahoo', start_date, end_date)


percent_change = 100*(panel_data['Close'] - panel_data['Open'])/panel_data['Open']


ax = percent_change.plot(kind='bar',figsize=(200,200),fontsize=100, title="percent change major indices per day")
ax.set_ylabel("percent change",size=100)
ax.legend(prop={'size': 100})

# moving averages for the closing price
# get average change per day
percent_change['mean'] = percent_change.mean(axis=1)


data = percent_change.copy()
data['positive'] = data['mean'] > 0

ax = data['mean'].plot(kind='bar', color=data.positive.map({True: 'g', False: 'r'}),figsize=(100,100),fontsize=100, title="percent change mean of indices per day")
ax.set_ylabel("percent change",size=100)
ax.legend(prop={'size': 100})


to_write = data[['mean','positive']]
to_write.to_csv('mean_finance.csv')

