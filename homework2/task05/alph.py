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
from typing import Any, List


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


def custom_range_2(
    seq: Any, key_word_first: Any = None, key_word_last: Any = None, step: Any = None
):

    first_el, last_el = None, None

    for i, el in enumerate(seq):
        if el == key_word_first:
            first_el = i
        if el == key_word_last:
            last_el = i

    if last_el is None:
        return [i for i in seq[0:first_el:step]]

    return [i for i in seq[first_el:last_el:step]]


print(custom_range_2(string.ascii_lowercase))
print(custom_range_2(string.ascii_lowercase, "g"))
print(custom_range_2(string.ascii_lowercase, "g", "p"))
print(custom_range(string.ascii_lowercase, "p", "g", -2))
