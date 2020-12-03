from unittest import TestCase, mock

import requests
from mock import patch
from task02.base_parser import count_dots_on_i, process_response


def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True

    elif r.status_code == 404:
        return False


print(count_dots_on_i("https://example.com"))


class FetchTests(TestCase):
    def test_returns_true_if_url_found(self):
        with patch("requests.get") as mock_request:
            url = "http://google.com"
            mock_request.return_value.status_code = 200

            self.assertTrue(url_exists(url))
            mock_request.assert_called_once_with(url)

    def test_returns_false_if_url_not_found(self):
        with patch("requests.get") as mock_request:
            url = "http://google.com/nonexistingurl"
            mock_request.return_value.status_code = 404

            self.assertFalse(url_exists(url))
            mock_request.assert_called_once_with(url)
