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
            buf = f.read(65536)
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
    for word in word_stream(file_path, encoding):
        pass


def get_rarest_char(file_path: str, encoding: str) -> str:
    pass


def count_punctuation_chars(file_path: str, encoding: str) -> int:
    pass


def count_non_ascii_chars(file_path: str, encoding: str) -> int:
    pass


def get_most_common_non_ascii_char(file_path: str, encoding: str) -> str:
    pass


isascii = lambda s: len(s) == len(s.encode())


for word in word_stream(file="simple_data.txt", encoding="utf-8"):
    print(word)
