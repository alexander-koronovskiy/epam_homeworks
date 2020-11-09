import pytest
from task01.handler_file import get_rarest_char


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        ("data00.txt", "x"),
    ],
)
def test_rarest_char(file: str, expected_result: str):
    """
    test for handler_file.py get_rarest_char method
    """
    actual_result = get_rarest_char(file)
    assert actual_result == expected_result
