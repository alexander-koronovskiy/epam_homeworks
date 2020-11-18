"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter
from typing import Generator, List


"""
прочитать слово до первого пробела или символа пунктуации
    обработать слово
    и уже реализовать эти операции отдельно.
    В идеале код питона должен читаться как документ с требованиями.
"""


def word_reader(file_path: str) -> Generator:
    with open(file_path, encoding="utf-8") as f:
        word = ""
        while True:
            ch = f.read(1).lower()
            # not char - end of word, end of read
            if not ch:
                break
            # char is punctuation - записать слово и знак
            # char is ' ' - конец слова
            yield ch


for i in word_reader("simple_data.txt"):
    print(i, end="")
