from pymongo import MongoClient
from HW22.db_config import get_db_name


class BaseDB:

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[get_db_name()]
        self.collection = ''

    def base_insert_one(self, data):
        self.db[self.collection].insert_one(data)

    def base_insert_many(self, data):
        self.db[self.collection].insert_many(data)

    def base_find_one(self):
        self.db[self.collection].find_one({})
