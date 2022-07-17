from pymongo import MongoClient


class BaseDB:
    client = MongoClient("mongodb://localhost:27017/")

    @staticmethod
    def base_insert_one(collection, data):
        collection.insert_one(data)

    @staticmethod
    def base_insert_many(collection, data):
        collection.insert_many(data)

    @staticmethod
    def base_find_one(collection):
        collection.find_one({})
