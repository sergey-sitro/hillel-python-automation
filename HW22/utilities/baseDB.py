from pymongo import MongoClient


class BaseDB:

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.collection = None

    def base_insert_one(self, data):
        self.insert_one(data)

    # def base_insert_many(collection, data):
    #     collection.insert_many(data)
    #
    # @staticmethod
    # def base_find_one(collection):
    #     collection.find_one({})
