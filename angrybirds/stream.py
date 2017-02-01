import tweepy
import json


class AngryBirdsStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if "retweeted_status" in status._json:
            return
        print(json.dumps(status._json, sort_keys=True, indent=4))

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
