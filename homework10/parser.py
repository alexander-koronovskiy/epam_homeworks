import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


url = "https://markets.businessinsider.com/index/components/s&p_500"
html_data = [row for row in parse_page(url).find_all("table")]

keys = []
for pos in html_data[1].find_all("th"):
    keys.append(" ".join(pos.text.split()))
print(list(filter(None, keys)))  # all keys for parse
