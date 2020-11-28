from task01.wrap import Memoize


@Memoize
def foo(a, b):
    return a * b


def test_memoize():
    foo(2, 4)
    foo("hi", 3)
    assert foo == {(2, 4): 8, ("hi", 3): "hihihi"}
