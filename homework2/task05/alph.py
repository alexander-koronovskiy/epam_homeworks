"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
import string
from typing import List


def custom_range(
    alphabet: str, start: str = "a", end: str = "z", pos: int = -2
) -> List[str]:

    count, pos_start, pos_end = 0, 1, 26

    for i in alphabet:
        if i == start:
            pos_start = count
        if i == end:
            pos_end = count
        count += 1

    return [i for i in alphabet[pos_start:pos_end:pos]]


print(custom_range(string.ascii_lowercase, "p", "g"))
