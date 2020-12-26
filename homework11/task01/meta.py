"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


class AttributeInitType(type):
    def __getattr__(self, item):
        if item in self.keys:
            return item
        raise AttributeError


class Colors(metaclass=AttributeInitType):
    keys = "RED", "BLUE", "ORANGE", "BLACK"


class Sizes(metaclass=AttributeInitType):
    keys = "XL", "L", "M", "S", "XS"
