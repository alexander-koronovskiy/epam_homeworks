from typing import List


def fb(n: int) -> List:
    """
    The standard program realization for calculation FizzBuzz sequence

    :param n: len of FizzBuzz sequence set by user
    :return: FizzBuzz sequence
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            continue
        if i % 3 == 0:
            result.append("Fizz")
            continue
        if i % 5 == 0:
            result.append("Buzz")
            continue
        result.append(i)
    return result
