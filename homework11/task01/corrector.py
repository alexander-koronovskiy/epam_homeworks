"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


class Enum(set):
    def __getattr__(self, __keys):
        if __keys in self:
            return __keys
        raise AttributeError


class MyMeta(type):
    def __new__(cls, name, baseClasses, classdict):
        return type.__new__(cls, name, baseClasses, classdict)


class ColorsEnum(metaclass=MyMeta):
    keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=MyMeta):
    keys = ("XL", "L", "M", "S", "XS")


Colors = Enum(["RED", "BLUE", "ORANGE", "BLACK"])
Sizes = Enum(["XL", "L", "M", "S", "XS"])

print(ColorsEnum.keys)
assert Colors.RED == "RED"
assert Sizes.XL == "XL"
