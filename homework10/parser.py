"""
====информация из основной таблицы на сайте====

- наименование компании +++
- ссылка на страницу +++
- годовая динамика в %

====информация на странице компании====

- последняя закрытая стоимость
- последняя открытая стоимость

- Код компании
- P/E компании справа от графика

- разница между '52 Week Low' и '52 Week High'
"""

import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


url = "https://markets.businessinsider.com/index/components/s&p_500"
html_data = [row for row in parse_page(url).find_all("table")]


names = []  # name, link, year_dynamics
for actions in html_data[1].find_all("a"):
    names.append(
        {
            "name": actions.text,
            "link": "https://markets.businessinsider.com/" + actions.get("href"),
        }
    )

print(names)
