from task01.wrap import Memoize


@Memoize
def foo(a, b):
    return a * b


def test_memoize():  # times =2
    foo(2, 4)  # first call
    foo("hi", 3)  # second call
    assert foo == {(2, 4): 8, ("hi", 3): "hihihi"}
    foo("g", 4)  # third call
    assert foo == {("g", 4): "gggg"}
