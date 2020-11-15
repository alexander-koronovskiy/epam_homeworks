from task03.std_handler import *

invalid_s = "error: file not found"
valid_s = "OK"


def test_errprint(capsys):
    """
    test for my_precious_logger in std_handler.py
    """
    my_precious_logger(valid_s)
    my_precious_logger(invalid_s)

    captured = capsys.readouterr()

    assert valid_s == captured.out
    assert invalid_s == captured.err
