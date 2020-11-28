"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса

Имя декоратора и методов неизменно
"""


class countcalls:
    "Decorator that keeps track of the number of times a function is called."

    __instances = {}

    def __init__(self, f):
        self.__f = f
        self.__numcalls = 0
        countcalls.__instances[f] = self

    def __call__(self, *args, **kwargs):
        self.__numcalls += 1
        return self.__f(*args, **kwargs)

    def count(self):
        "Return the number of times the function f was called."
        return countcalls.__instances[self.__f].__numcalls

    @staticmethod
    def counts():
        "Return a dict of {function: # of calls} for all registered functions."
        return dict(
            [
                (f.__name__, countcalls.__instances[f].__numcalls)
                for f in countcalls.__instances
            ]
        )


# example
@countcalls
def f():
    return "f called"


@countcalls
def g():
    return "g called"


f()
f()
f()
print(f.count())  # prints 3
print(countcalls.counts())  # same as f.counts() or g.counts()
g()
print(g.count())  # prints 1
