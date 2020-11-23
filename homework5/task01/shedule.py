"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework) Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
"""


class Homework:
    """
    1. Homework принимает на вход 2 атрибута:
    text - текст задания,  и количество дней на это задание

    Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством дней на выполнение

    created - c точной датой и временем создания

    Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean
    """

    def __init__(self, text, deadline):
        """Constructor"""
        self.text = text
        self.doors = deadline

    created = ""


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
