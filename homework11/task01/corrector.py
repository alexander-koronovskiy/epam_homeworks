"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


def meth():
    print("Calling method")


class MyMeta(type):
    @classmethod
    def __prepare__(cls, name, baseClasses):
        return {"meth": meth}

    def __new__(cls, name, baseClasses, classdict):
        return type.__new__(cls, name, baseClasses, classdict)

    def __getattr__(self, __keys):
        if __keys in self:
            return __keys
        raise AttributeError


class ColorsEnum(metaclass=MyMeta):
    keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=MyMeta):
    keys = ("XL", "L", "M", "S", "XS")


print(ColorsEnum.keys)
