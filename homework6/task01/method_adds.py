"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса

Имя декоратора и методов неизменно
"""


def get_created_instances(self):
    print("Success")


class InsertMethod:
    def __init__(self, methodToInsert):
        self.methodToInsert = methodToInsert

    def __call__(self, classObject):
        def wrapper(*args, **kwargs):
            setattr(classObject, self.methodToInsert.__name__, self.methodToInsert)
            return classObject(*args, **kwargs)

        return wrapper


@InsertMethod(get_created_instances)
class User(object):
    def __init__(self):
        pass

    def action(self):
        self.action()
