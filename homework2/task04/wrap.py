"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from functools import lru_cache
from typing import Callable


def cache(func: Callable) -> Callable:
    @lru_cache
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def memorize(func):
    cache = dict()

    def memorized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memorized_func
