import pytest
from tasks.fib import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1, 2, 3, 5, 8, 13, 21], True),
        ([7, 8, 9, 10, 12], False),
    ],
)
def test_check_fibonacci(value: [int], expected_result: bool):
    """
    test for fib.py check_fibonacci method
    use 'pytest test_fib.py' in console log for testing
    """
    actual_result = check_fibonacci(value)
    assert actual_result == expected_result
