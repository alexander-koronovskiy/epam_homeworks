from task03.std_handler import *

invalid_s = "error: file not found"
valid_s = "OK"


def test_errprint(capsys):
    errprint(invalid_s)
    captured = capsys.readouterr()
    assert invalid_s == captured.err
