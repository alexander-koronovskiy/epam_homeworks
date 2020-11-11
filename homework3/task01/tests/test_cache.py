from task01.wrap import *


@Memoized(cache_size=2)
def f():
    return input("? ")


def test_cache():
    """
    for testing this i used 'pytest -s'
    """
    assert f()
