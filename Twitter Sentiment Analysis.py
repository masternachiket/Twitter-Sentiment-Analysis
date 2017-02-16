# Twitter Sentiment Analysis
import tweepy
from textblob import TextBlob


consumer_key = 'Your Consumer Key'
consumer_secret = 'Your Consumer Secret Key'

access_token = 'Your Access Tokens Key'
access_token_secret = 'Your Access Token Secret Key'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Key_Word")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
