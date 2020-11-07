import pytest
from task04.check_sum import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, -1, 0], [1, 1, 2], [-1, 0, -3], [1, -2, 3], 11),
    ],
)
def test_check_fibonacci(a: [int], b: [int], c: [int], d: [int], expected_result: 11):
    """
    test for fib.py check_sum_of_four method
    use 'pytest test_check_sum.py' in console log for testing
    """
    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == expected_result
