from unittest import mock

from task02.base_parser import fetch_webpage


def test_fetch_with_mock():
    with mock.patch("requests.get") as mock_get:

        username = "https:/www.example.com"
        mock_get.return_value.ok = True

        json_response = (
            "<html><head>A song</head><body>House of the Rising Sun</body></html>"
        )
        mock_get.return_value.json.return_value = json_response

        info = fetch_webpage(username)
        assert info is not None
        assert json_response == info
