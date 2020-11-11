import pytest
from task02.fib import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0], False),
        ([0, 1], True),
        ([0, 1, 1], True),
        ([2, 3, 5], False),
        ([0, 1, 1, 2, 3, 5, 8], True),
        ([0, 1, 1, 2, 3, 8], False),
    ],
)
def test_check_fibonacci(value: [int], expected_result: bool):
    """
    test for fib.py check_fibonacci method
    use 'pytest test_fib.py' in console log for testing
    """
    actual_result = check_fibonacci(value)
    assert actual_result == expected_result
