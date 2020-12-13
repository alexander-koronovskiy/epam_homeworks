"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt: 1 3 5
file2.txt: 2 4 6
    list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def readInChunks(fileObj: str, chunkSize: int = 2048) -> Iterator:
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.

    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


def int_handler(a: str) -> List:
    """
    search int values at string
    it works with no divided value
    :return:
    """
    num_list = []

    num = ""
    for char in a:
        if char.isdigit() or char == "-":
            num = num + char
        else:
            if num != "":
                num_list.append(int(num))
                num = ""
    if num != "":
        num_list.append(int(num))
    return num_list


f1 = open("file1.txt")
f2 = open("file2.txt")
for stream in [f1, f2]:
    for chunk in readInChunks(stream):
        print(sorted(int_handler(chunk)))  # преобразовать числа в строке
    stream.close()
