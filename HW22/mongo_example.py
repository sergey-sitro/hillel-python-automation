from pymongo import MongoClient
import bson

my_client = MongoClient("mongodb://localhost:27017/")

mydb = my_client["users_db"]
my_collection = mydb['users']

# user_1 = {'_id': bson.ObjectId(), 'name': 'Peter', 'age': 45, 'email': 'peter@gmail.com'}

# users_list = [
#     {'_id': bson.ObjectId(), 'name': 'Peter', 'age': 45, 'email': 'peter@gmail.com'},
#     {'_id': bson.ObjectId(), 'name': 'Viktoria', 'age': 55, 'email': 'viktoria@gmail.com'},
#     {'_id': bson.ObjectId(), 'name': 'Alan', 'age': 75, 'email': 'alan@gmail.com'}
# ]

# my_user = my_collection.insert_one(user_1)
# new_users = my_collection.insert_many(users_list)

# print(new_users.inserted_ids)
user = my_collection.find_one({})
# print(user)
user = my_collection.find_one({'name': 'Alan'})
# print(user)
users = my_collection.find()
for u in users:
    print(u)

my_client.close()
