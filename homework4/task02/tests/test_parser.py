from task02.base_parser import *


def test_parser():
    """
    comparison of function results with measured value
    """
    url = "https://python-scripts.com/file-exists"
    assert count_dots_on_i(url) == 30
