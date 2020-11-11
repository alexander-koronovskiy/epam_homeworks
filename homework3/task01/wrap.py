"""
In previous homework task 4, you wrote a cache function
that remembers other function output value.
Modify it to be a parametrized decorator,
so that the following code:
"""

from functools import lru_cache
from typing import Callable


def cache(func: Callable) -> Callable:
    @lru_cache
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
