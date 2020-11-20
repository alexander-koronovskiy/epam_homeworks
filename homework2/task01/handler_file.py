from collections import Counter
from typing import List

from task01.reader import *


def get_longest_diverse_words(file_path: str, encoding: str) -> List[str]:

    """
    Find 10 longest words consisting from largest amount of unique symbols
    """

    # init searching longest diverse words
    most_unique_words = []
    permit_unique_len = 0

    for word in word_stream(file_path, encoding):

        # don't add elements, that contains very few unique symbols
        if len(set(word)) > permit_unique_len:
            most_unique_words.append((word, len(set(word))))

        # if words less then 10, permit all recordings
        if len(most_unique_words) > 10:
            most_unique_words.sort(key=lambda unique: unique[1], reverse=True)
            permit_unique_len = most_unique_words.pop(-1)[1]

    return [i[0] for i in most_unique_words]


def get_rarest_char(file_path, encoding) -> str:

    """
    Find rarest symbol for document
    """

    # storage for all symbols
    ch_map = {}
    for word in word_stream(file_path, encoding):
        for ch in word:
            if ch in ch_map:
                ch_map[ch] += 1
            else:
                ch_map[ch] = 1

    # sort char map, and find rarest element
    min_unique = sorted(ch_map.items(), key=lambda item: item[1])

    return min_unique[0][0]


def count_punctuation_chars(file_path: str, encoding: str) -> int:
    """
    Count every punctuation char
    """
    count = 0
    for word in word_stream(file_path, encoding):
        for symbol in word:
            if unicodedata.category(symbol).startswith("P"):
                count += 1
    return count


def count_non_ascii_chars(file_path: str, encoding: str) -> int:
    """
    Count every non ascii char
    """
    non_ascii_count = 0
    for word in word_stream(file_path, encoding):
        for ch in word:
            if not ch.isascii():
                non_ascii_count += 1
    return non_ascii_count


def get_most_common_non_ascii_char(file_path: str, encoding: str) -> str:
    """
    Get most common non ascii char
    """
    non_asciis = ""
    for word in word_stream(file_path, encoding):
        for ch in word:
            if not ch.isascii():
                non_asciis += ch
    return Counter(non_asciis).most_common()[0][0]


isascii = lambda s: len(s) == len(s.encode())
