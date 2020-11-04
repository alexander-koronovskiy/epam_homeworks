from typing import Tuple

import pytest
from tasks.max_and_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        ("tasks/numbers.txt", (0, 9)),
    ],
)
def test_max_sub_sum(file: str, expected_result: Tuple[int, int]):
    """
    test for fib.py check_fibonacci method
    use 'pytest test_fib.py' in console log for testing
    """
    actual_result = find_maximum_and_minimum(file)
    assert actual_result == expected_result
