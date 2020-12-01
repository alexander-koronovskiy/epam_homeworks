import timeit

from task02.fast_calc import create_threads, pm_calc


def test_thread_solution():
    """
    test origin solution in threads for fast_calc.py
    """
    start_calc = timeit.default_timer()
    create_threads(500)
    end_calc = timeit.default_timer()
    assert end_calc - start_calc < 10


def test_pm_solution():
    """
    test new solution in Pool.map for fast_calc.py
    """
    assert pm_calc(5) < 3


if __name__ == "__main__":
    test_thread_solution()
    test_pm_solution()
