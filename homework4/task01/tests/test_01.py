from task01.file_handler import os, read_magic_number

# file creation, recording data
corr_f_name = "data_correct.txt"
incorr_f_name = "data_incorrect.txt"
empty_f_name = "empty_f.txt"
not_exist_f_name = "not_exist_f.txt"

corr_f = open(corr_f_name, "tw", encoding="utf-8")
corr_f.write("2.4789654646456456 \n56 88 \n12")
corr_f.close()

incorr_f = open(incorr_f_name, "tw", encoding="utf-8")
incorr_f.write("13 \n77")
incorr_f.close()

empty_f = open(empty_f_name, "tw", encoding="utf-8").close()


def test_magic_number(capsys):
    """
    value test for file_handler.py
    """
    assert read_magic_number(corr_f_name)
    assert read_magic_number(incorr_f_name) == ValueError
    assert read_magic_number(empty_f_name) == ValueError
    assert read_magic_number(not_exist_f_name) == ValueError


# files remove
os.remove(corr_f_name)
os.remove(incorr_f_name)
os.remove(empty_f_name)


def test_exist() -> bool:
    """
    temp files exist test for file_handler.py after it's work
    """
    assert not os.path.isfile(corr_f_name)
    assert not os.path.isfile(incorr_f_name)
    assert not os.path.isfile(empty_f_name)
    assert not os.path.isfile(not_exist_f_name)
