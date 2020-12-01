from task03.filter import *


def foo(x):
    return x ** 2 == 36


def foo_first(x):
    return x % 2 == 0


def test_my():
    Filter(foo(5))
    sample_usage = Filter(foo_first, foo)
    sample_usage.apply(data=range(10)) == [6]


# example of usage:
# should return only even numbers from 0 to 99
def test_origin():
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(100)) == [i for i in range(1, 100) if i % 2 == 0]
