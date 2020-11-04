import pytest
from tasks.sub_arrays import find_maximal_sub_array_sum


@pytest.mark.parametrize(
    ["array", "chunk", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
    ],
)
def test_max_sub_sum(array: [int], chunk: int, expected_result: bool):
    """
    test for fib.py check_fibonacci method
    use 'pytest test_fib.py' in console log for testing
    """
    actual_result = find_maximal_sub_array_sum(array, chunk)
    assert actual_result == expected_result
