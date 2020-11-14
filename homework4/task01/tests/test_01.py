from task01.file_handler import *

# 1 file creation, recording data
f = open("corr.txt", "tw", encoding="utf-8")
f.write("2 \n56 88 \n12")
f.close()

f1 = open("inc.txt", "tw", encoding="utf-8")
f1.write("13 \n77")
f1.close()

f2 = open("emp.txt", "tw", encoding="utf-8").close()
f3 = "not_exist.txt"


def test_exist() -> bool:
    """
    #2 file exist test for file_handler.py
    """
    assert os.path.isfile("corr.txt")
    assert os.path.isfile("inc.txt")
    assert os.path.isfile("emp.txt")
    assert not os.path.isfile("not_exist.txt")


def test_magic_number():
    """
    #3 value test for file_handler.py
    """
    assert read_magic_number("corr.txt")
    assert read_magic_number("inc.txt") == ValueError
    assert read_magic_number("emp.txt") == ValueError
    assert read_magic_number("not_exist.txt") == ValueError


# 4 file remove
# 5 temp file don't exist check
