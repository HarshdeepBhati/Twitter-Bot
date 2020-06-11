import tweepy
import time

CONSUMER_KEY = 'apP89c3tu6vvN4bHHh4JWKaV7'
CONSUMER_SECRET='z70AtlOTrzSq5DztYEJTQl3JOdxxM2rtvH0KldumXiaREQJ1sg'

ACCESS_KEY='1270944859763798016-p0hgyjCdE0FI9W9GPl06nFsGmSly4j'
ACCESS_SECRET='xFFFtDyKc0uLrlwxsgyI0mUvry5A5hBNDHK7SjFDlqP2C'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

hashtag = '#cancelPTUexams'
tweetnumber = 100

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(1)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(1)

searchBot()