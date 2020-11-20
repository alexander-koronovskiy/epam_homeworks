from task01.handler_file import *


def test_longest_diverse_words():
    assert (
        get_longest_diverse_words("task01/texts/simple_data.txt", encoding="utf-8")[0]
        == "memory"
    )


def test_rarest_char():
    assert get_rarest_char("task01/texts/simple_data.txt", encoding="utf-8") == "'"


def test_punctuation_chars():
    assert (
        count_punctuation_chars("task01/texts/simple_data.txt", encoding="utf-8") == 3
    )


def test__non_ascii_chars():
    assert (
        count_non_ascii_chars("task01/texts/data.txt", encoding="unicode-escape") > 1000
    )
    assert (
        count_punctuation_chars("task01/texts/simple_data.txt", encoding="utf-8") == 4
    )


def test_most_common_non_ascii_char():
    assert (
        get_most_common_non_ascii_char(
            "task01/texts/data.txt", encoding="unicode-escape"
        )
        == "ä"
    )
