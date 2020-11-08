"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:

    with open(file_name) as f:
        seq = list(map(int, f.readline().split()))
        min_seq, max_seq = min(seq), max(seq)

    with open(file_name) as f:
        for line in f.readlines():
            seq = list(map(int, line.split()))

            min_seq = min(seq) if min_seq > min(seq) else min_seq
            max_seq = max(seq) if max_seq < max(seq) else max_seq

    return min_seq, max_seq
