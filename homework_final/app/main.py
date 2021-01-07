import datetime

from peewee import *
from randomuser import RandomUser

# Generate a single user
user = RandomUser()

# create db
db = SqliteDatabase("posts.db")


# Generate a list of 10 random users
class User(Model):

    first_name = TextField()
    last_name = TextField()
    gender = TextField()
    phone = TextField()
    email = TextField()
    state = TextField()

    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


def add_row():
    user = RandomUser.generate_users(1)[0]

    initialize_db()
    User.create(
        first_name=user.get_first_name(),
        last_name=user.get_last_name(),
        gender=user.get_gender(),
        phone=user.get_phone(),
        email=user.get_email(),
        state=user.get_state(),
    ).save()


def get_row():
    db.connect()
    row = User.get(User.id == 7)
    db.close()
    return row


# add_row()
print(get_row().phone)
