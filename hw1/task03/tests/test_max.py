from typing import Tuple

import pytest
from task03.max_and_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        ("numbers.txt", (-13, 99)),
        ("numbers00.txt", (1, 5)),
    ],
)
def test_max_sub_sum(file: str, expected_result: Tuple[int, int]):
    """
    test for max_and_min.py find_maximum_and_minimum method
    use 'pytest test_max.py' in console log for testing
    """
    actual_result = find_maximum_and_minimum(file)
    assert actual_result == expected_result
