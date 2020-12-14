from task03.count_file_lines import os, universal_file_counter


def test_line_counter():
    """
    task 03 homework 9 test
    """
    path = os.path.dirname(__file__)
    assert universal_file_counter(path, "txt", str.split) == 6
    assert universal_file_counter(path, "txt") == 6
