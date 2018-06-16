# based on https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

import tweepy, time, sys 

from credentials import *
from generate_advertisement import get_ad

# INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True: 
    print("about to get ad...")
    ad = get_ad()
    api.update_status(ad)
    time.sleep(INTERVAL)