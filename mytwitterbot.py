import tweepy
import time

CONSUMER_KEY = 'apP89c3tu6vvN4bHHh4JWKaV7'
CONSUMER_SECRET='z70AtlOTrzSq5DztYEJTQl3JOdxxM2rtvH0KldumXiaREQJ1sg'

ACCESS_KEY='1270944859763798016-p0hgyjCdE0FI9W9GPl06nFsGmSly4j'
ACCESS_SECRET='xFFFtDyKc0uLrlwxsgyI0mUvry5A5hBNDHK7SjFDlqP2C'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


FILE_NAME = "last_seen_id.txt"
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):

        if '#ultimatebot' in tweet.full_text.lower():
            print(str(tweet.id)+' - '+ tweet.full_text)
            api.update_status("@"+tweet.user.screen_name+' '+"Hi! I am the bot created by @harshdeep0028 :) and I am retweeting back!!!", tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(10)


