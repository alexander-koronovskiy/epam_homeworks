from typing import Any, List

import pytest
from task03.combination import combinations


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ],
)
def test_combination(inp: List[Any], expected_result: List[List]):
    """
    test for combination.py
    """
    actual_result = combinations(*inp)
    assert actual_result == expected_result
