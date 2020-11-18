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

"""
прочитать слово до первого пробела или символа пунктуации
    обработать слово
    и уже реализовать эти операции отдельно.
    В идеале код питона должен читаться как документ с требованиями.
"""


forbidden = (".", "?", "!", ":", ";", "-", "—", " ", "[", "]")


def word_reader(file_path: str) -> Generator:
    with open(file_path, encoding="utf-8") as f:
        while True:

            # buffer creation
            buf = f.read(10240)
            if not buf:
                break

            # word boundary check
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch

            record = ""
            words = []

            # work with buffer
            for symbol in buf:

                # recording word
                record += symbol

                if symbol.isspace():
                    words.append(record)
                    record = ""

            # word stream
            for word in words:
                yield word


for word in word_reader("simple_data.txt"):
    print(word)
