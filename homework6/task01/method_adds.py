"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса

Имя декоратора и методов неизменно
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        print("hello !")
        func(*args, **kwargs)

    return wrapper


class A:
    @decorator
    def smth_method(a="???"):
        return "this is one of method of " + a


print(A.smth_method())
