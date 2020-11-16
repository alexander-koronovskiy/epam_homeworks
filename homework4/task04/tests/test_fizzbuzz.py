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


def test_fb_default():
    """
    How to use

    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository <path your repository>
    - Checkout branch <your branch>
    - Open terminal
    - Write 'pytest' in console log
    - Test done with default number n = 20
    """
    assert fb(default_n) == default_res
