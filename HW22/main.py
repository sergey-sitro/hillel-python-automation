from HW22.collections.users_collection import UsersCollection
import pymongo
import bson

# UsersCollection().insert_user({'_id': bson.ObjectId(), 'name': 'Peter Griffin', 'age': 45, 'email': 'peterg@gmail.com'})
# UsersCollection().insert_users([
#     {'_id': bson.ObjectId(), 'name': 'Homer Simpson', 'age': 45, 'email': 'homers@gmail.com'},
#     {'_id': bson.ObjectId(), 'name': 'Randy Marsh', 'age': 35, 'email': 'randym@gmail.com'},
#     {'_id': bson.ObjectId(), 'name': 'Eric Cartman', 'age': 9, 'email': 'ericc@gmail.com'}
# ])

print(UsersCollection().get_user())

