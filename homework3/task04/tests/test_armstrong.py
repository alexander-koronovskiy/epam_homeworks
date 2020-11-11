from task04.armstrong import is_armstrong


def test_armstrong():
    """
    test for fast_calc.py
    """
    assert is_armstrong(153) == True
    assert is_armstrong(10) == False
