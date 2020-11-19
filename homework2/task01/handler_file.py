"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
from typing import Generator, List


def word_stream(file: str, encoding: str) -> Generator:
    with open(file, encoding=encoding) as f:
        while True:

            # buffer creation
            buf = f.read(65536).lower()
            if not buf:
                break

            # word boundary check
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch

            # work with buffer content
            record = ""
            words = []

            # regard that divided by punctuation word is a some different words
            for symbol in buf:
                if unicodedata.category(symbol).startswith("P"):
                    words.extend(record.split())
                    words.append(symbol)
                    record = ""
                else:
                    record += symbol

            for word in words:
                yield word


def get_longest_diverse_words(file_path: str, encoding: str) -> List[str]:

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

    # it saves symbol and occurrence
    ch_map = {}

    for word in word_stream(file_path, encoding):
        for ch in word:
            if ch in ch_map:
                ch_map[ch] += 1
            else:
                ch_map[ch] = 1

    min_unique = sorted(ch_map.items(), key=lambda item: item[1])
    return min_unique[0][0]


def count_punctuation_chars(file_path: str, encoding: str) -> int:
    count = 0
    for word in word_stream(file_path, encoding):
        if len(word) == 1:
            count += 1
    return count


def count_non_ascii_chars(file_path: str, encoding: str) -> int:
    pass


def get_most_common_non_ascii_char(file_path: str, encoding: str) -> str:
    pass


isascii = lambda s: len(s) == len(s.encode())
# for word in word_stream(file="data.txt", encoding="unicode-escape"): print(word)  # 0
# print(get_longest_diverse_words("simple_data.txt", encoding="utf-8"))  # 1
# print(get_rarest_char("simple_data.txt", encoding="utf-8"))  # 2
print(count_punctuation_chars("simple_data.txt", encoding="utf-8"))
