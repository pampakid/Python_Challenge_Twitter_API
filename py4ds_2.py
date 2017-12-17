# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:16:31 2017

@author: Pampa Kid
"""

import tweepy
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from my_keys import *
import warnings
warnings.filterwarnings('ignore')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

#Sentiment Intensitiy Analyzer
analyzer = SentimentIntensityAnalyzer()

# Target users input

#Target Account for each Media Source
target_user = ["@BBC","@CBS","@Fox","@CNN","@nytimes"]

# Variables for holding sentiments
sentiments = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):
    
   
    #loop through each Media Source
    for target in target_user:
        # Get all tweets from home feed
        public_tweets = api.user_timeline(target)
             

        # Loop through all tweets 
        for tweet in public_tweets:
            
            
        # Run vaderSentiment on each tweet
            results = analyzer.polarity_scores(tweet["text"])
            compound = results["compound"]
            pos = results["pos"]
            neu = results["neu"]
            neg = results["neg"]
            
           
        
            # Add sentiments for each tweet into an array
            sentiments.append({"Date": tweet["created_at"],
                               "Screen_Name": tweet['user']['screen_name'],
                               "Compound": compound,
                               "Positive": pos,
                               "Negative": neu,
                               "Neutral": neg})


#Generated dataframe containing sentiment for Media Sources
df_sentiment_analysis= pd.DataFrame(sentiments) 

#display head of df_sentiment_analysis 
df_sentiment_analysis.head()

#Save df_sentiment_analysis as a csv titled, 'Sentiment_analyzer_Twitter.csv'.
df_sentiment_analysis.to_csv('Sentiment_analyzer_Twitter.csv',index=False)

#Plot of Sentiment Analysis of Media Tweets
x_values = np.arange(1,df_BBC.shape[0]+1)


plt.figure(figsize=(10,5))
plt.scatter(x_values[::-1],df_BBC['Compound'],edgecolors='black',label='BBC')


plt.scatter(x_values[::-1],df_CBS['Compound'],edgecolors='black',label = 'CBS')
plt.scatter(x_values[::-1],df_CNN['Compound'],edgecolors='black',color='yellow',label='CNN')
plt.scatter(x_values[::-1],df_fox['Compound'],edgecolors='black',color='b',label='Fox')
plt.scatter(x_values[::-1],df_nytimes['Compound'],edgecolors='black',color='green',label='New York Times')

plt.legend(frameon=True,shadow= True,edgecolor='black',fontsize = 'large', title='Media Sources', bbox_to_anchor=(1, 1))
plt.xlim(0,100)
plt.xlabel('Tweets Ago',fontsize='18')
plt.ylabel('Tweet Polarity',fontsize='18')

now = datetime.now()
now = now.strftime("%m/%d/%Y")
plt.title('Sentiment Analysis of Media Tweets ({})'.format(now),fontsize=(18))

plt.xlim(100,0);
###################################
##### Get Tweets & Save Them ######
###################################

#def label(analysis, threshold = 0):
#	if analysis.sentiment[0]>threshold:
#		return 'Positive'
#	else:
#		return 'Negative'
