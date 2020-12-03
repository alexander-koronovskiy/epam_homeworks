from task02.base_parser import count_dots_on_i


def connection_mock(url):
    return {"message": "OK"}


def test_connection():
    assert connection_mock("https://example.com/") == {"message": "OK"}


def test_count():
    """
    comparison of function results with measured value
    """
    url = "https://example.com/"
    assert count_dots_on_i(url) == 59
