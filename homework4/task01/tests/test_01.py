from task01.file_handler import *


def test_exist() -> bool:
    """
    file exist test for file_handler.py
    """
    assert os.path.isfile("correct.txt")
    assert os.path.isfile("incorrect.txt")
    assert os.path.isfile("empty.txt")
    assert not os.path.isfile("not_exist.txt")


def test_magic_number():
    assert read_magic_number("correct.txt")
    assert not read_magic_number("incorrect.txt")
    assert not read_magic_number("empty.txt")
    assert not os.path.isfile("not_exist.txt")
