import datetime

from peewee import *

db = SqliteDatabase("posts.db")


class Homework(Model):
    id = PrimaryKeyField()
    date = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    text = TextField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Homework], safe=True)
    db.close()


initialize_db()
homework = Homework.create(id=2, title="Some title", text="some text1")
homework.save()
