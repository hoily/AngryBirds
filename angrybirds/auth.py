import tweepy
import os

auth = tweepy.OAuthHandler(os.environ["ANGRY_BIRDS_CONSUMER_KEY"], os.environ["ANGRY_BIRDS_CONSUMER_SECRET"])
auth.set_access_token(os.environ["ANGRY_BIRDS_ACCESS_TOKEN"], os.environ["ANGRY_BIRDS_ACCESS_TOKEN_SECRET"])
