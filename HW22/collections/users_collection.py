from HW22.utilities.baseDB import BaseDB


class UsersCollection(BaseDB):
    users_db = BaseDB().client["users_db"]
    users_collection = users_db['users']

    def __init__(self, collection=users_collection):
        super().__init__()
        self.collection = collection

    def insert_user(self, data):
        return BaseDB.base_insert_one(self.collection, data)

    # def insert_users(self, data):
    #     return BaseDB.base_insert_many(self.collection, data)
    #
    # def get_user(self):
    #     got_user = BaseDB.base_find_one(self.collection)
    #     return got_user
