"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


class Enum:
    def __init__(self, *args):
        self.__keys = args

    def __getattr__(self, key):
        if key in self.__keys:
            return key
        raise AttributeError


Colors = Enum("RED", "BLUE", "ORANGE", "BLACK")
Sizes = Enum("XL", "L", "M", "S", "XS")


class Singleton(type):
    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class Meta:
    __metaclass__ = Singleton

    def __init__(self, a=None):
        self.a = a


c = Meta("parameter")
print(c.a)
