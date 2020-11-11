import timeit

from task02.fast_calc import *


def test_calculate():
    """
    test for fast_calc.py
    """
    start_calc = timeit.default_timer()
    create_threads(500)
    end_calc = timeit.default_timer()
    assert end_calc - start_calc < 60
