"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""


def flatten(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            yield from flatten(key)
            yield from flatten(value)
    elif isinstance(obj, (list, tuple, set)):
        for item in obj:
            yield from flatten(item)
    else:
        yield obj


def count(it, elem):
    c = 0
    for item in it:
        if item == elem:
            c += 1
    return c


def count_2(obj, elem):
    c = 0
    if isinstance(obj, dict):
        for key, value in obj.items():
            c += count_2(key, elem)
            c += count_2(value, elem)
    elif isinstance(obj, (list, tuple, set)):
        for item in obj:
            c += count_2(item, elem)
    elif obj == elem:
        c += 1
    return c
