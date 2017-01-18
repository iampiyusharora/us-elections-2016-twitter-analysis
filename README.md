# Data Analysis and Sentiment Analysis of US Elections 2016

This is a python based project. Let's get into how to run this.

First you need to have all the basic necessary libraries installed. (Rest can be installed once you run the files, the terminal will tell you the missing libraries)

How this project works?

#Open this file: twitter_streaming.py

You need to enter your access token, access token secret, consumer key and consumer secret. If you don't know how and where to get those, Google can guide you very easily. It's a piece of cake.

You also need to add keywords in the same file. See the last section of the code:

#This line filter Twitter Streams to capture data by the keywords.
    stream.filter(track=['elections2016', 'trump', 'hillary'])

#Once, this is done, you can run the file.

This will start streaming tweets from  Twitter. I needed to test huge amount of data, hence, I ran it for 3 days and I had around 3 Gigs of Data.

#Now, you need to run this command in another terminal to save the streaming data into a txt file:

python twitter_streaming.py > twitter_data.txt

#Next, you need to run analyze_tweets.py

This is where the magic happens. This will take some time, if you have huge amount of data.

This will give you a graph of Top 5 languages that are used for tweets related to Trump and Hillary.

Further, another graph will tell you Top 5 countries that are tweeting about Trump and Hillary.

#Sentiment Analysis

We have 2 txt files in this project: positive.txt and negative.txt

They are a list of Positive and Negative Keywords.

When you run sentiment.py

First the code will add each of the keywords in a list. Then we read our file which has all of the tweets, we do some preprocessing of the tweets, remove punctuations, and make all the words in to lowercase.

Further, we create 2 counters, for positve and negative tweets and initialize them from zero. Then we count the total number of words, in each tweets and try to see,

If there is any word that matches with our list of positive or negative keyword. If we have a positve keyword, we increase our counter from zero to +1, similarly for negative.

Finally, then we create a score of our poritive and negative sentiment. positive_counter/total_word_count in tweets.

An output .csv file is created with the positive and negative score of the tweets.

The output graphs are also stored in the folder final_putput.zip.

Hope this helps someone. Cheers!!



