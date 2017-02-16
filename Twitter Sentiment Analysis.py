# Twitter Sentiment Analysis
import tweepy
from textblob import TextBlob

# Requirements
consumer_key = 'Your Consumer Key'
consumer_secret = 'Your Consumer Secret Key'
access_token = 'Your Access Tokens Key'
access_token_secret = 'Your Access Token Secret Key'

# Authenticating with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Searching for tweets with Key_Word
public_tweets = api.search("Key_Word")

# Printing out all the tweets with Analysis
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
