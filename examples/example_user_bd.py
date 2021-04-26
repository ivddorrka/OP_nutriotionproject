# add containing folder to path to be able import user_db module
import sys
sys.path.insert(1, '../')

from user_db import *

# Initialize UserDB
user_db = UserDB()

# Create Users
user1 = User('user1', '1234')
user2 = User('user2', 'pwd')
user3 = User('user3', 'top_secret')


# get non-existing user, exception will be raised and handled
try:
    print(user_db.get('user1'))
except UserNotFound:
    print('Trying to get non-existing user')

user_db.add(user1)
user_db.add(user2)
user_db.add(user3)

# add already existing user, exception will be raised and handled
try:
    user_db.add(user3)
except UserAlreadyExists:
    print('Trying to add the same user second time')

print('Print user_db with all users:  ', user_db)
print('Print poped user1 object:      ', user_db.pop('user1'))
print('Print user_db after pop:       ', user_db)
user_db.clear()
print('Print user_db after clear:     ', user_db)

# get non-existing user (which was deleted by clear method), exception will be raised and handled
try:
    user_db.pop('user3')
except UserNotFound:
    print('Trying to get non-existing user (it was deleted previously)')

