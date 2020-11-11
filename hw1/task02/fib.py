"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    stat = False
    if data[:2] == [0, 1]:
        stat = True
        for i in range(2, len(data)):
            stat = data[i] == data[i - 1] + data[i - 2]
            if not stat:
                return False
    return stat


print(check_fibonacci([0, 1, 1]))
