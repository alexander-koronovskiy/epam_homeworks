import pytest
from task05.sub_arrays import find_maximal_sub_array_sum


@pytest.mark.parametrize(
    ["array", "chunk", "expected_result"],
    [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16), ([4, 9, -3, -2, -1], 3, 13)],
)
def test_max_sub_sum(array: [int], chunk: int, expected_result: int):
    """
    test for test_arr.py find_maximal_sub_array_sum method
    use 'pytest test_arr.py' in console log for testing
    """
    actual_result = find_maximal_sub_array_sum(array, chunk)
    assert actual_result == expected_result
