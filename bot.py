import tweepy
import time
import os

# Fetch Twitter API credentials from environment variables
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def fetch_liked_tweets():
    liked_tweets = api.favorites(count=10)  # Fetch the last 10 liked tweets
    return liked_tweets

def repost_tweet(tweet_id):
    try:
        api.retweet(tweet_id)
        print(f"Retweeted: {tweet_id}")
    except tweepy.TweepError as e:
        print(f"Error retweeting: {e}")

def main():
    liked_tweets = fetch_liked_tweets()
    for tweet in liked_tweets:
        repost_tweet(tweet.id)

if __name__ == "__main__":
    main()
