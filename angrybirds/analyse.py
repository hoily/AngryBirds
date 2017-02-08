from .mongo import get_db, get_collection, insert_document
from .sentiment import get_analysis


def analyse_tweets():
    db = get_db()
    collection = get_collection('raw_tweets', db)
    for tweet in collection.find({}):
        insert_document({
            "id": tweet["id"],
            "text": tweet["text"],
            "user_id": tweet["user"]["id"],
            "user_followers_count": tweet["user"]["followers_count"],
            "timestamp": tweet["timestamp_ms"],
            "sentiment": get_analysis(tweet["text"])
        }, 'tweets')
