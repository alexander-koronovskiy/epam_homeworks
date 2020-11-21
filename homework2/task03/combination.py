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
from typing import Any, List, Tuple


def combs(xs, i=0) -> Tuple[Any]:
    """
    xs - elements sequence
    :returns all element combination
    """
    if i == len(xs):
        yield ()
        return
    for c in combs(xs, i + 1):
        yield c
        yield (xs[i],) + c


def expand(lst: List[List]) -> List[int]:
    """
    expand list
    """
    total = []
    for element in lst:
        if type(element) == type([]):
            total.extend(expand(element))
        else:
            total.append(element)
    return total


def combinations(*args) -> List[Any]:
    """
    function that takes K lists as arguments and returns all possible
    lists of K items where the first element is from the first list,
    the second is from the second and so one.
    """
    lst = [i for i in args]
    tmp = lst.copy()
    result = []

    for current in lst:
        for elem in lst:
            if elem == current:
                tmp.remove(current)

                for i in current:
                    for j in expand(tmp):
                        result.append([i, j])
    return result
