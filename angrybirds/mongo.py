from pymongo import MongoClient


def get_db():
    client = MongoClient('localhost', 27017)
    return client['angry-birds']


def get_collection(collection_name, db):
    return db[collection_name]


def insert_document(document, collection_name):
    db = get_db()
    collection = get_collection(collection_name, db)
    collection.insert_one(document)


def remove_document(document, collection_name):
    db = get_db()
    collection = get_collection(collection_name, db)
    collection.delete_one(document)
