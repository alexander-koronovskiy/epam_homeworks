import requests
from bs4 import BeautifulSoup


def parse_tabs(url: str) -> int:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return [tabs for tabs in soup.find_all("table")]


url = "https://markets.businessinsider.com/index/components/s&p_500"
for td in parse_tabs(url):
    print(td)
print(len(parse_tabs(url)))


# получение элементов таблицы с определенным тэгом
# обработка данных
