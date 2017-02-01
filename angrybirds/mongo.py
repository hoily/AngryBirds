from pymongo import MongoClient


def get_db():
    client = MongoClient('localhost', 27017)
    db = client['angry-birds']
    return db


def get_collection(collection_name, db):
    collection = db[collection_name]
    return collection


def insert_document(document, collection_name):
    db = get_db()
    collection = get_collection(collection_name, db)
    collection.insert_one(document)
