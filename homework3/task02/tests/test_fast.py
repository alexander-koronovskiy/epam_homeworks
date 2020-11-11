import timeit

from task02.fast_calc import slow_calculate


def test_calculate():
    """
    test for fast_calc.py
    """
    start_calc = timeit.default_timer()
    slow_calculate(0)
    end_calc = timeit.default_timer()
    assert end_calc - start_calc < 4
