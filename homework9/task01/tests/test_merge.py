from task01.merge_sort_files import merge_sorted_files


def test_num():
    """
    task 01 homework 9 test
    """
    assert merge_sorted_files("file1.txt", "file2.txt") == [-1, 2, 3, 4, 5, 6]
