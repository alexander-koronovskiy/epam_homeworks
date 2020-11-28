"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса

Имя декоратора и методов неизменно
"""


class SomeClass:

    # constructor
    def __init__(self, number):
        self.number = number

    # bound_method
    @classmethod
    def create_new_object(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    @staticmethod
    def just_function():
        return "I cannot change class instance"

    def print_me(self):
        return self.number


foo = SomeClass
bar = SomeClass(10)

print(foo.create_new_object(5).print_me(), bar.print_me())
