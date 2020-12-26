"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


class MyMeta(type):
    def __new__(cls, name, baseClasses, classdict):
        return type.__new__(cls, name, baseClasses, classdict)


class ColorsEnum(metaclass=MyMeta):
    keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=MyMeta):
    keys = ("XL", "L", "M", "S", "XS")


class Enum:
    def __init__(self, *args):
        self.__keys = args

    def __getattr__(self, key):
        if key in self.__keys:
            return key
        raise AttributeError


Colors = Enum("RED", "BLUE", "ORANGE", "BLACK")
Sizes = Enum("XL", "L", "M", "S", "XS")

assert Colors.RED == "RED"
assert Sizes.XL == "XL"
print(ColorsEnum.keys)
