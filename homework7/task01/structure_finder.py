"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Dict, Generator, List


def traverse(d: Dict) -> Generator:
    for key, val in d.items():
        if isinstance(val, dict):
            yield from traverse(val)

        else:
            yield val


def expand(lst: List[List]) -> List:
    """
    expand list
    """
    total = []
    for element in lst:
        if isinstance(element, list):
            total.extend(expand(element))
        else:
            total.append(element)
    return total
