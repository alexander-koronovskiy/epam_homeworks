from typing import Tuple

import pytest
from task02.major_and_minor import major_and_minor_elem


@pytest.mark.parametrize(
    ["inp", "expected_result"],
    [([3, 2, 3], (3, 2)), ([2, 2, 1, 1, 1, 2, 2], (2, 1))],
)
def test_major_and_minor(inp: [int], expected_result: Tuple[int, int]):
    """
    test for major_and_minor.py get_rarest_char method
    """
    actual_result = major_and_minor_elem(inp)
    assert actual_result == expected_result
