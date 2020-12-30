import datetime

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
    Атрибуты:

    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством дней на выполнение
    created - c точной датой и временем создания
    """

    id = PrimaryKeyField()
    text = TextField()
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Teacher(Model):
    """
    Атрибуты: last_name, first_name

    Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    """

    id = PrimaryKeyField()
    name = CharField()
    last_name = CharField()

    class Meta:
        database = db


class Student(Model):
    """
    Атрибуты: last_name, first_name

    Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
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


def get_row():
    db.connect()
    print(Homework.get(Homework.id == 1).created)
    db.close()


if __name__ == "__main__":
    get_row()
