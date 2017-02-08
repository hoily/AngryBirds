import tweepy
from .mongo import insert_document


class AngryBirdsStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if "retweeted_status" in status._json:
            return
        insert_document(status._json, 'tweets')
        print('{0}: {1}'.format(status._json["user"]["screen_name"],
                                status._json["text"]))

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
