#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd
from textblob import TextBlob
import nltk
from numpy.random import choice

df = pd.read_csv('cleaned_tweets.csv')

# in this file i compute the sentiment analyisis for all the tweets
def calculate_sentiment(df):
   sentiments = {}
   for date in df.columns:
      text = df[date]
      positive, negative, neutral = 0,0,0
      for tweet in text:
         analysis = TextBlob(str(tweet))
         if analysis.sentiment[0]>0:
            positive+=1
         elif analysis.sentiment[0]<0:
            negative+=1
         else:
            neutral+=1
         sentiments[date] = [negative,neutral,positive]
   return sentiments

sentiments = calculate_sentiment(df)
# sentiments
# dump into json
with open('sentiments_day_tweets.json', 'w') as fp:
    json.dump(sentiments, fp)




