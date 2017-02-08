import tweepy
from .mongo import insert_document


class AngryBirdsStreamListener(tweepy.StreamListener):
    def should_ignore(self, status):
        return any([
            "retweeted_status" in status,
            status['lang'] != "en"
        ])

    def on_status(self, status):
        if self.should_ignore(status._json):
            return
        insert_document(status._json, 'raw_tweets')
        print('{0}: {1}'.format(status._json["user"]["screen_name"],
                                status._json["text"]))

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
