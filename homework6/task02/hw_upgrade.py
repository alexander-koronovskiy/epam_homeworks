"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework) Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
"""
from datetime import *


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

    # Format example: 2019-05-26 16:44:30.688762
    date_select = datetime.now() - timedelta(days=3)

    def __init__(self, text: str, deadline: int):
        """Constructor"""
        self.text = text
        self.created = self.date_select
        self.deadline = self.created + timedelta(days=deadline)

    def is_active(self):
        return datetime.now() < self.deadline


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
        return "You are late" if not hw.is_active() else ""


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
