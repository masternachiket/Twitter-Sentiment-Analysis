# Twitter Sentiment Analysis
import tweepy
from textblob import TextBlob


consumer_key = '61I2LUkkdF2tcgj92NGmvRQCY'
consumer_secret = 'wifamBJUlKRDZHB7gjmIlBtdoRDL6D0ZinPBppDr3KXIYDXD3x'

access_token = '2998264597-66o8Af3MUUsDaCpNmQ4qKhUIvkIO3Yec9xrU3GU'
access_token_secret = 'PtQ1d05Q8E3E4fASLHindk30XrCw0M0NoEQf7Tx5XCAMk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
