# Sentiment analysis of tweets and the correlation to stock market performance


## step 1 collect , clean and analyze twitter data

I used tweepy (library to standarizes twitter api) to collect twitter data for a specific time range.
I took several steps to clean the data. I removed stop words, using stop words from the nltk library corpus. I also removed punctuation and the 20 most common and 20 least common words. I used the Textblob library to autocorrect tweets. 

I used the Textblob library to analyse the sentiment, I partitioned the tweets based on the score into positive, neutral and negative tweets. 

# twitter sentiment per day results

![alt text](https://github.com/red-starter/capstone/blob/master/graphs/better_chart.png)


# initial chart data
![alt text](https://github.com/red-starter/capstone/blob/master/graphs/each_index_change.png)
# aggregated chart data
![alt text](https://github.com/red-starter/capstone/blob/master/graphs/percent_change.png)
# results analysis
![alt text](https://github.com/red-starter/capstone/blob/master/graphs/alllinestogether.png)
