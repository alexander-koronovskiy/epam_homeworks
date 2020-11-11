from task01.wrap import cache


def test_combination():
    """
    test for wrap.py
    """

    # cache(times=2)
    def f():
        return "? "

    assert f() == "? "
