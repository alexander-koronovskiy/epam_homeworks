"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, List


def expand(lst: List[Any]) -> List[int]:
    """
    expand list
    """
    total = []
    for element in lst:
        if type(element) == type([]):  # not element
            total.extend(expand(element))
        else:
            total.append(element)
    return total
