from task05.fizzbuzz_gen import fiz


def test_fiz():
    """
    FizzBuzz generator check with default n
    """
    numbers = range(1, 2 ** 20)

    # this gets one number, turns that one number into fuz, repeat
    assert " ".join(fiz(numbers))
