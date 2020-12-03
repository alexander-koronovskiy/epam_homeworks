from mock import patch
from task02.base_parser import count_dots_on_i, process_response


def test_response_content_is_not_empty():
    with patch("requests.get") as mock_request:
        url = "example.com"
        mock_request.return_value.content = "iii content"
        response = count_dots_on_i(url)
        assert response == 3


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
