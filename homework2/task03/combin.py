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


def combinations(*args: List[Any]) -> List[List]:
    comb1 = itertools.combinations(args[0], 1)
    comb2 = itertools.combinations(args[1], 1)
    combs = itertools.product(comb1, comb2)
    result = [list(itertools.chain.from_iterable(x)) for x in combs]
    return result


print(combinations([1, 2], [3, 4]))
