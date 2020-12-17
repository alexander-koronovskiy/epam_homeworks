import requests
from bs4 import BeautifulSoup


def parse(url: str) -> int:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    yield [quotes for quotes in soup.find_all("p")]


url = "https://markets.businessinsider.com/index/components/s&p_500"
for q in parse(url):
    print(q)
