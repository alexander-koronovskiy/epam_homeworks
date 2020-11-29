from task01.wrap import cache


@cache(3)
def power(a, b):
    return a ** b


@cache(2)
def foo(a, b):
    return a * b


def test_power_two_times_cache():
    """
    Test for test func 'power' in cache times = 3
    """
    assert power(3, 5) == {(3, 5): 243}
    assert power(2, 3) == {(3, 5): 243, (2, 3): 8}
    assert power(3, 4) == {(3, 5): 243, (2, 3): 8, (3, 4): 81}


def test_foo_two_times_cache():
    """
    Test for test func 'foo' in cache times = 2
    """
    assert foo("hi", 3) == {("hi", 3): "hihihi"}
    assert foo(2, 3) == {("hi", 3): "hihihi", (2, 3): 6}
    assert foo(3, 5) == {(2, 3): 6, (3, 5): 15}
