import datetime
from datetime import timedelta

from peewee import (
    CharField,
    DateTimeField,
    Model,
    PrimaryKeyField,
    SqliteDatabase,
    TextField,
)

db = SqliteDatabase("posts.db")


class Homework(Model):
    """
    text - текст задания
    created - хранит объект datetime.timedelta c точной датой и временем создания
    """

    id = PrimaryKeyField()
    text = TextField()
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Teacher(Model):
    """
    Атрибуты: last_name, first_name
    """

    id = PrimaryKeyField()
    name = CharField()
    last_name = CharField()

    class Meta:
        database = db


class Student(Model):
    """
    Атрибуты: last_name, first_name
    """

    id = PrimaryKeyField()
    name = CharField()
    last_name = CharField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Homework], safe=True)
    db.close()


def add_row():
    initialize_db()
    homework = Homework.create(id=1, title="Base python", text="")
    homework.save()


def get_deadline(deadline: int) -> datetime:
    """
    deadline - количество дней на выполнение
    возвращает точное время дедлайна
    """
    db.connect()
    row = Homework.get(Homework.id == 1).created
    db.close()
    return row + timedelta(days=deadline)
