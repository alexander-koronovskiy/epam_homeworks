from task05.fizzbuzz_gen import fb

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


def test_fb_default():
    """
    FizzBuzz generator check with default n
    """
    for i, item in enumerate(fb(default_n)):
        assert default_res[i] == item
