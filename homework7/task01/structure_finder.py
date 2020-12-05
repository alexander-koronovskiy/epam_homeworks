"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Iterable, List


def traverse(d):
    for key, val in d.items():
        if isinstance(val, dict):
            yield from traverse(val)
        else:
            yield val
