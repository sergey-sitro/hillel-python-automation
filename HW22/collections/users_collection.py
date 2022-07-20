from HW22.utilities.baseDB import BaseDB


class UsersCollection(BaseDB):

    def __init__(self):
        super().__init__()
        self.collection = self.client['users_db']['users']

    def insert_user(self, data):
        return BaseDB.base_insert_one(self.collection, data)

    # def insert_users(self, data):
    #     return BaseDB.base_insert_many(self.collection, data)
    #
    # def get_user(self):
    #     got_user = BaseDB.base_find_one(self.collection)
    #     return got_user
