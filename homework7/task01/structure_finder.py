"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""


class Counts:

    count = []

    def recursive(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                self.count.append(key)
                self.recursive(value)

        elif isinstance(obj, list) or isinstance(obj, tuple):
            for item in obj:
                self.recursive(item)
        else:
            self.count.append(obj)

        return self.count
