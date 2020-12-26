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
