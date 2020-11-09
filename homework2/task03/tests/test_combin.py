from typing import Any, List

import pytest
from task03.combin import combinations


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ],
)
def test_major_and_minor(inp: List[Any], expected_result: List[List]):
    """
    test for major_and_minor.py get_rarest_char method
    """
    actual_result = combinations(inp)
    assert actual_result == expected_result
