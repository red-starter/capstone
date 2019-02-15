#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tweet_sentiment_df = pd.read_csv('all_days.csv')
mean_finance_df = pd.read_csv('mean_finance.csv')

mean_finance_df = mean_finance_df.set_index('Date').rename(columns ={'mean':'agg_stock_percent_change'})
tweet_sentiment_df = tweet_sentiment_df.T

tweet_sentiment_df['total'] =  tweet_sentiment_df[0]+tweet_sentiment_df[1]+tweet_sentiment_df[2]
tweet_sentiment_df['percentange_positive_tweets'] = tweet_sentiment_df[2]/tweet_sentiment_df['total']*100
tweet_sentiment_df['percentange_negative_tweets'] = tweet_sentiment_df[0]/tweet_sentiment_df['total']*100


tweet_sentiment_df = tweet_sentiment_df.rename(columns ={0:'negative_tweets',1:'neutral_tweets',2:'positive_tweets'})
# inner join on date index
joined_df = mean_finance_df.join(tweet_sentiment_df, how='inner')

# plot the percentages
df = joined_df[['agg_stock_percent_change','percentange_positive_tweets','percentange_negative_tweets']]
df.plot(figsize=(16,9),title="percent change major indices per day",linestyle='-', marker='o')

# calculate the spearman correlation
r_pos = df['agg_stock_percent_change'].corr(df['percentange_positive_tweets'],method='spearman')
r_neg = df['agg_stock_percent_change'].corr(df['percentange_negative_tweets'],method='spearman')
# (0.2972073812865935, -0.2917632840717102)

# calculate the T values
# http://www.sthda.com/english/wiki/correlation-test-between-two-variables-in-r
N = len(joined_df)
def t_value(rs,n):
    return rs/pow(1-rs**2,0.5)*pow(n-2,0.5)

t_value_pos = t_value(r_pos,N) 
t_value_neg = t_value(r_neg,N) 

# statistical significance alpha = 0.05
# get the pavalue pvalue 
pval1 = stats.t.sf(np.abs(t_value_pos), N-2)  # one-sided pvalue = Prob(abs(t)>t
pval2 = stats.t.sf(np.abs(t_value_neg), N-2)  # one-sided pvalue = Prob(abs(t)>t
print('p value',pval1,pval2)





