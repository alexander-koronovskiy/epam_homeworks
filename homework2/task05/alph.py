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
from typing import Any, List


def custom_range(
    seq: Any, key_word_first: Any = None, key_word_last: Any = None, step: Any = None
) -> List[Any]:

    first_el, last_el = None, None

    for i, el in enumerate(seq):
        if el == key_word_first:
            first_el = i
        if el == key_word_last:
            last_el = i

    if last_el is None:
        return [i for i in seq[0:first_el:step]]

    return [i for i in seq[first_el:last_el:step]]
