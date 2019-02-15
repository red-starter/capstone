# Sentiment analysis of tweets and the correlation to stock market performance

First Null hypothesis 
- the # of positive tweets on a given day is positively correlated to stock market performance
First Alternative Hypothesis 
- the # of positive tweets on a given day is not correlated to stock market performance

Second Null hypothesis 
- the # of negative tweets on any given day is negatively correlated to stock market performance
Second Alternative Hypothesis 
- the # of negative tweets on a given day is not correlated to stock market performance

## Collection and cleaning and analysis of tweets

I used tweepy (library to standarizes twitter api) to collect twitter data for a specific time range.
I took several steps to clean the data. I removed stop words, using stop words from the nltk library corpus. I also removed punctuation and the 20 most common and 20 least common words. I used the Textblob library to autocorrect tweets. 

I used the Textblob library to analyse the sentiment, I partitioned the tweets based on the score into positive, neutral and negative tweets. 

The textblob library has a training set with preclassified movie reviews, and it uses a NaiveBayes classifier to classify the new text's polarity from +1 (positive) to -1 (negative). 
source code is : https://github.com/sloria/TextBlob/blob/90cc87ab0f9e25f37379079840ec43aba59af440/textblob/en/sentiments.py


### twitter sentiment per day results

![alt text](https://github.com/red-starter/capstone/blob/master/graphs/better_chart.png)

## Collection of stockmarket data
In order to approximate the stock market perforamce I collected data , using python datareader library on the following indices 
- "SPY", iShares Core S&P 500 ETF 
- "IVV", Vanguard Total Stock Market ETF 
- "VTI", Vanguard S&P 500 ETF 
- "VOO", PowerShares QQQ 
- "QQQ", iShares Russell 2000 
- "IWM", SPDR Dow Jones Industrial Average 

I calculated the performace for each day by getting the (closing - opening) percentage

# Performance of stock indices
![alt text](https://github.com/red-starter/capstone/blob/master/graphs/each_index_change.png)

afterwards, I averages the perforance for each day across all the indices

# Aggregated average performance of stock indices
![alt text](https://github.com/red-starter/capstone/blob/master/graphs/percent_change.png)

I normalized the positive and negative tweets as a percentage , here is the final chart tracking the percentage change of the stocks market and the fraction of collected tweets that were negative or positive for a given day. I did an inner join on the date indices of each data set.

# Results analysis
![alt text](https://github.com/red-starter/capstone/blob/master/graphs/alllinestogether.png)

The spearman correlation was calculared between the mean stock market performance and the percentange of positive tweets and the negative tweets.  

### The results were `0.2972` and `-0.2917` respectively. 

I used a statistical significance alpha = 0.05

Deriving the T values from the spearman correlation were `-1.64` and `1.67` 

The derived p values were `0.0522` and `0.0556` respectively.

### Since p > 0.05 in both cases,  I was unable to reject my null hypothesis in either case.
