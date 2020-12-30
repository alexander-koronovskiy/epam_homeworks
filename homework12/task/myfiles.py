import datetime

from peewee import *

db = SqliteDatabase("posts.db")


class Homework(Model):
    """
    Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством дней на выполнение
    created - c точной датой и временем создания
    """

    id = PrimaryKeyField()
    date = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    text = TextField()

    class Meta:
        database = db


class Teacher(Model):
    """"""

    id = PrimaryKeyField()
    date = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    text = TextField()

    class Meta:
        database = db


class Student(Model):
    """"""

    id = PrimaryKeyField()
    date = DateTimeField(default=datetime.datetime.now)
    first_name = CharField()
    text = TextField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Homework], safe=True)
    db.close()


def add_row():
    initialize_db()
    homework = Homework.create(id=8, title="Some title", text="some text1")
    homework.save()


db.connect()
print(Homework.get(Homework.id == 1).date)
db.close()
