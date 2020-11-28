"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса

Имя декоратора и методов неизменно
"""


def get_created_instances(cls):
    def helper(*args, **kwargs):
        helper.calls += 1
        return cls(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = cls.__name__
    return helper


def reset_instance_counter(cls):
    def helper(*args, **kwargs):
        helper.calls = 0
        return cls(*args, **kwargs)

    helper.__name__ = cls.__name__
    return helper
