from task04.fizzbuzz import fb

default_n = 20
default_res = [
    1,
    2,
    "Fizz",
    4,
    "Buzz",
    "Fizz",
    7,
    8,
    "Fizz",
    "Buzz",
    11,
    "Fizz",
    13,
    14,
    "FizzBuzz",
    16,
    17,
    "Fizz",
    19,
    "Buzz",
]


# mb add optional test for getting result by n
def test_fb_default():
    """
    FizzBuzz sequence check with default n
    """
    assert fb(default_n) == default_res
