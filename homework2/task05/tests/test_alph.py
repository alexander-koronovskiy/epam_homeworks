import string

import pytest
from task05.alph import custom_range


@pytest.mark.parametrize(
    ["alphabet", "start", "end", "pos", "expected_result"],
    [
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
    ],
)
def test_custom_range(alphabet, start, end, pos, expected_result):
    """
    test for alph.py
    """
    actual_result = custom_range(alphabet, start, end, pos)
    assert actual_result == expected_result
