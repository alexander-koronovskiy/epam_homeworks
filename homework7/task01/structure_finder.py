"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Iterable, List


def some_useful_func(lst):
    return ["{}.{}".format(key, val) for key, vals in lst.items() for val in vals]
