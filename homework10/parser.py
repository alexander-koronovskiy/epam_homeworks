"""

1. список информации с главной

1.1. годовая динамики в % на главной
1.1.1 перевод в рубли (можно сделать в выводе)
1.2 последняя открытая/закрытая стоимость

2. парсинг с сылок информации о компаниях

2.1. Код компании
2.2. P/E компании справа от графика
2.3 разница между '52 Week Low' и '52 Week High'

3. склейка в словарь, обработка данных
"""

import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


url = "https://markets.businessinsider.com/index/components/s&p_500"
html_data = [row for row in parse_page(url).find_all("table")]

# dict(name: costs, per year info -> str)
vals = []
for pos in html_data[1].find_all("td"):
    vals.append(" ".join(pos.text.split()))
vals = list(filter(None, vals))

# chosen info from main table
main_table_info = [" ".join(i) for i in zip(vals[1::8], vals[7::8])]

# src_pages
src_pages = [
    "https://markets.businessinsider.com/" + link.get("href")
    for link in html_data[1].find_all("a")
]

# parsing from link list (async ?)
# zip, and handle information

# tests
print(src_pages)
