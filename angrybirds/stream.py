import tweepy
from auth import auth

api = tweepy.API(auth)


class AngryBirdsStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


streamListener = AngryBirdsStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamListener)

stream.filter(track=['python'])
