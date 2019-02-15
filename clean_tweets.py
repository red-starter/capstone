#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from textblob import TextBlob
import nltk

# Removal of Stop Words
nltk.download('stopwords')
from nltk.corpus import stopwords

df = pd.read_json('./files/parsed_tweets.json')

# Removing Punctuation
df = df.str.replace('[^\w\s]','')
stop = stopwords.words('english')

#Common words
freq = pd.Series(' '.join(df.stack()).split()).value_counts()
most_common = freq[:20]
least_common = freq[-20:]

set_most_common = list(most_common.index)
set_least_common = list(least_common.index)
to_remove = stop + set_most_common + set_least_common
to_remove_set = set(to_remove)

#remove common words and uncommon and stopwords
for col in df.columns:
    df[col] = df[col].str.lower()
    df[col] = df[col].apply(lambda x: " ".join(x for x in x.split() if x not in to_remove_set))

#spelling correction
# takes to long to run
# helps with duplicates
for col in df.columns:
    df[col] = df[col].apply(lambda x: str(TextBlob(x).correct()))

# outputs
df.to_csv("./files/cleaned_tweets.csv", index=False)



