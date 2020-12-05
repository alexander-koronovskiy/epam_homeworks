"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    ...


class Helper:
    def __init__(self, entry="Default"):
        self.entry = entry

    content = []

    def expand(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                self.content.append(key)
                self.expand(value)

        elif isinstance(obj, list) or isinstance(obj, tuple):
            for item in obj:
                self.expand(item)
        else:
            self.content.append(obj)

        return self.content
