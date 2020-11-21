"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import Any, List


def combs(xs, i=0):
    if i == len(xs):
        yield ()
        return
    for c in combs(xs, i + 1):
        yield c
        yield (xs[i],) + c


def expand(lst):
    total = []
    for element in lst:
        if type(element) == type([]):
            total.extend(expand(element))
        else:
            total.append(element)
    return total


lst = [[1, 2], [3, 4]]
tmp = lst.copy()
result = []

current = lst[0]

for elem in lst:
    if elem == current:
        tmp.remove(current)

        for i in current:
            for j in expand(tmp):
                result.append([i, j])

print(result)
