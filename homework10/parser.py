import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


url = "https://markets.businessinsider.com/index/components/s&p_500"
html_data = [row for row in parse_page(url).find_all("table")]
print(html_data[1].find_all("th"))  # text.split() - keys for dictionary


# получение элементов таблицы с определенным тэгом
# обработка данных
