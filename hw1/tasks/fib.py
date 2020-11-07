"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    return not (False in [check_number(i) for i in data][1:])


def check_number(n: int) -> bool:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if n == b or n == a:
            return True
    return False
