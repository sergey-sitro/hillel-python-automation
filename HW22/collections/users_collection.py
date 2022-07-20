from HW22.utilities.baseDB import BaseDB


class UsersCollection(BaseDB):

    def __init__(self):
        super().__init__()
        self.collection = 'users'

    def insert_user(self, data):
        return self.base_insert_one(data)

    def insert_users(self, data):
        return self.base_insert_many(data)

    def get_user(self):
        user = self.base_find_one()
        print(user)
