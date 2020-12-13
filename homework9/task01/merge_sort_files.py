"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt: 1 3 5
file2.txt: 2 4 6
    list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path

# from typing import List, Union, Iterator


def readInChunks(fileObj, chunkSize=2048):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 2kB.

    """
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


f1 = open("file1.txt")
f2 = open("file2.txt")
for chunk in zip(readInChunks(f1), readInChunks(f2)):
    print(chunk)
f1.close()
