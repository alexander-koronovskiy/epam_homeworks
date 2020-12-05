"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""


def recursive(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            print(key)
            recursive(value)
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for item in obj:
            recursive(item)
    else:
        print(obj)
