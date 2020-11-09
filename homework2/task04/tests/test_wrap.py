from task04.wrap import cache


def test_combination():
    """
    test for wrap.py
    """

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
