"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_file_content(file_path: str) -> str:
    s = ""

    with open(file_path) as f:
        while True:
            ch = f.read(1).lower()
            s += ch
            if not ch:
                break

    return s


def get_longest_diverse_words(file_path: str) -> List[str]:
    unique_map = {}
    s = get_file_content(file_path)
    words = s.split()

    for word in set(words):
        unique_map[word] = len(set(word))

    max_unique = sorted(unique_map.items(), key=lambda item: item[1], reverse=True)
    return [i[0] for i in max_unique[:10]]


def get_rarest_char(file_path: str) -> str:
    s = get_file_content(file_path)
    ch_map = {}

    for ch in s:
        if ch in ch_map:
            ch_map[ch] += 1
        else:
            ch_map[ch] = 1

    min_unique = sorted(ch_map.items(), key=lambda item: item[1])
    return min_unique[0][0]


def count_punctuation_chars(file_path: str) -> int:
    s = get_file_content(file_path)
    punctuation_count = 0

    for ch in s:
        if not (ch.isdigit() or ch.isalpha() or ch.isspace()):
            punctuation_count += 1

    return punctuation_count


f1 = get_rarest_char("data00.txt")
print(f1)
