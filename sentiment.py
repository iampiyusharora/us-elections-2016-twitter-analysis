from __future__ import division
import urllib
import csv
from string import punctuation


files=['negative.txt','positive.txt','twitter_data.txt']


tweets = open("twitter_data.json").read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]


for tweet in tweets_list:
    positive_counter=0
    negative_counter=0
    
    tweet_processed=tweet.lower()
    
    
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1
        
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print len(positive_counts)
print len(negative_counts)

output=zip(tweets_list,positive_counts,negative_counts)

writer = csv.writer(open('tweet_sentiment.csv', 'wb'))
writer.writerows(output)


#Notes
#So, we have a list of positive keywords and negative keywords in a text file. We read both of those files, 
#and
# add each of the keywords in a list. Then we read our file which has all of the tweets, we do some preprocessing of the tweets, remove punctuations, and make all the 
#words in to lowercase.
# then we create 2 counters, for positve and negative tweets and initialize them from zero. Then we count the total number of words, in each tweets and try to see,
#if there is any word that matches with our list of positive or negative keyword. If we have a positve keyword, we increase our counter from zero to +1, 
# similarly for negative.
# then we create a score of our poritive and negative sentiment. positive_counter/total_word_count in tweets.


#

