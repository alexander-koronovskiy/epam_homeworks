import datetime

from peewee import *

# create database to interact with
db = SqliteDatabase("posts.db")


# create a class for blogposts
class Post(Model):
    id = PrimaryKeyField()
    date = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    text = TextField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Post], safe=True)
    db.close()


# if db tables are not created, create them
# add a new row
# persist it to db, not necessarily needed
initialize_db()
post = Post.create(id=1, title="Some title", text="some text1")
post.save()
