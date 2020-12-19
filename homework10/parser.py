"""
==== 1 словарь имя-ссылка ==== (завершено)

- наименование компании
- ссылка на страницу

==== 2 словарь имя-строка с ссылки ====

- Код компании
- P/E компании справа от графика
- разница между '52 Week Low' и '52 Week High'

==== 3 словарь имя-строка с главной ====

- годовая динамики в % на главной
- последняя открытая/закрытая стоимость

получить 2 словарь, сложить с третьим
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

print(vals[::8])
print(vals[1::8])
print(vals[7::8])

companies_main = {}

# dict(name: link)
companies_link = {}
for link in html_data[1].find_all("a"):
    companies_link[link.text] = "https://markets.businessinsider.com/" + link.get(
        "href"
    )

# dict(name: parse data from link)
companies_personal = {}
