from task02.base_parser import *


def test_parser():
    """
    comparison of function results with measured value
    """
    url = "https://example.com/"
    assert count_dots_on_i(url) == 59
