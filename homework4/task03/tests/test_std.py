from task03.std_handler import *


def test_errprint(capsys):  # or use "capfd" for fd-level
    errprint("world\n")
    captured = capsys.readouterr()
    assert captured.err == "world\n"
