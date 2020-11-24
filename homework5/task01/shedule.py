"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework) Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

# 1 преобразовать строку в дату
# 2 homework-log, сохранение д.з.


"""
import datetime


class Homework:
    """
    1. Homework принимает на вход 2 атрибута:
    text - текст задания, и, deadline - количество дней на это задание

    Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством дней на выполнение
    created - c точной датой и временем создания

    Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
    """

    def __init__(self, text: str, deadline: str):
        """Constructor"""
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now()


class Student:
    """
    2. Student

    Атрибуты: last_name, first_name

    Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
    """

    def __init__(self, first_name, last_name):
        """Constructor"""
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, hw: Homework):
        return hw.is_active()


class Teacher:
    """
    3. Teacher

    Атрибуты: last_name, first_name

    Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework

    Для работы этого метода не требуется сам объект.
    """

    def __init__(self, first_name, last_name):
        """Constructor"""
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, data):
        return Homework(text, data)
