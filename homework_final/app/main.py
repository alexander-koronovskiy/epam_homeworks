from peewee import *
from randomuser import RandomUser

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

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


# start app
def load_rows():

    initialize_db()

    for user in RandomUser.generate_users(10):
        User.create(
            first_name=user.get_first_name(),
            last_name=user.get_last_name(),
            gender=user.get_gender(),
            phone=user.get_phone(),
            email=user.get_email(),
            state=user.get_state(),
        ).save()


# upload app
def show_rows():
    db.connect()
    users_selected = (
        User.select()
        .where(User.id < 10)
        .limit(5)
        .order_by(User.id.desc())
        .dicts()
        .execute()
    )
    row = [user for user in users_selected]
    db.close()
    return row


# add_rows()
print(show_rows())
