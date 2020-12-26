"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
"""


class Enum(set):
    def __getattr__(self, __keys):
        if __keys in self:
            return __keys
        raise AttributeError


Animals = Enum(["DOG", "CAT", "HORSE"])
ColorsEnum = Enum(["RED", "BLUE", "ORANGE", "BLACK"])
SizesEnum = Enum(["XL", "L", "M", "S", "XS"])

assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
