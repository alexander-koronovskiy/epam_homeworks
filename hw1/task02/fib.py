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
        for i in range(len(data)):
            stat = data[i] == data[i - 1] + data[i - 2]
    return stat
