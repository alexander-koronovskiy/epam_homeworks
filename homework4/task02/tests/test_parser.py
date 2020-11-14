from task02.base_parser import *

url = "https://python-scripts.com/file-exists"


def test_parser():
    print(get_html(url))
    assert True
