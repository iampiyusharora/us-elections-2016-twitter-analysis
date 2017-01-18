
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False



def main():


	#Reading Tweets
	print 'Reading Tweets\n'
	tweets_data_path = 'twitter_data.txt'
	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue


	#Structuring Tweets
	print 'Structuring Tweets\n'
	tweets = pd.DataFrame()
	tweets['text'] = [tweet.get('text','') for tweet in tweets_data]
	tweets['lang'] = [tweet.get('lang','') for tweet in tweets_data]
	tweets['country'] = [tweet['place']['country'] if "place" in tweet and tweet['place']
                      else np.nan for tweet in tweets_data]




	#Analyzing Tweets by Language
	print 'Analyzing tweets by language\n'
	tweets_by_lang = tweets['lang'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
	plt.savefig('tweet_by_lang', format='png')


	#Analyzing Tweets by Country
	print 'Analyzing tweets by country\n'
	tweets_by_country = tweets['country'].value_counts()
	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Countries', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
	tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
	plt.savefig('tweet_by_country', format='png')



if __name__=='__main__':
	main()





