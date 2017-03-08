from .mongo import get_db, get_collection, insert_document, remove_document
from .words import get_keywords
from .sentiment import get_analysis


def analyse_tweets():
    db = get_db()
    collection = get_collection('raw_tweets', db)
    for tweet in collection.find({}):
        keywords = list(get_keywords(tweet["text"]))
        if keywords:
            insert_document({
                "id": tweet["id"],
                "text": tweet["text"],
                "user_id": tweet["user"]["id"],
                "user_followers_count": tweet["user"]["followers_count"],
                "timestamp": tweet["timestamp_ms"],
                "sentiment": get_analysis(tweet["text"]),
                "keywords": keywords
            }, 'tweets')
        remove_document({"id": tweet["id"]}, 'raw_tweets')
