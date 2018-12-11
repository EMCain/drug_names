import time
import tweepy

from src.tweet import Account
from lib.generate import generate

# from credentials import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

account = Account(
    CONSUMER_KEY=CONSUMER_KEY,
    CONSUMER_SECRET=CONSUMER_SECRET,
    ACCESS_KEY=ACCESS_KEY,
    ACCESS_SECRET=ACCESS_SECRET
)

while True:
    print("about to get ad...")
    generate(account)
    time.sleep(INTERVAL)
