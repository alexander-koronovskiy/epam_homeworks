from typing import Generator


def fiz(n) -> Generator:
    """
    realization for FizzBuzz generator

    :param n: len of FizzBuzz generator set by user
    :return: FizzBuzz generator
    """
    for i in n:
        if i % 15 == 0:
            yield "fizbuz"
        elif i % 5 == 0:
            yield "buz"
        elif i % 3 == 0:
            yield "fiz"
        else:
            yield str(i)
