import pytest
from task01.calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (1, True),
        (0, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    """
    test for calc.py test_power_of_2 method
    use 'pytest test_calc.py' in console log for testing
    """
    actual_result = check_power_of_2(value)
    assert actual_result == expected_result
