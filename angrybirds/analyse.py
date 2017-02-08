import .mongo
import .sentiment


def analyse_tweets():
    db = mongo.get_db()
    collection = mongo.get_collection('raw_tweets', db)
    for tweet in collection.find({}):
        mongo.insert_document({
            "id": tweet["id"],
            "text": tweet["text"],
            "user_id": tweet["user"]["id"],
            "user_followers_count": tweet["user"]["followers_count"],
            "timestamp": tweet["timestamp_ms"],
            "sentiment": sentiment.get_analysis(tweet["text"])
        }, 'tweets')
