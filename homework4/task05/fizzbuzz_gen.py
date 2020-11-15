from typing import Generator


def fb(n: int) -> Generator:
    """
    realization for FizzBuzz generator

    :param n: len of FizzBuzz generator set by user
    :return: FizzBuzz generator
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
            continue
        elif i % 3 == 0:
            yield "Fizz"
            continue
        elif i % 5 == 0:
            yield "Buzz"
            continue
        else:
            yield i
