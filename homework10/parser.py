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

#  just list of parameters
keys = []
for pos in html_data[1].find_all("th"):
    keys.append(" ".join(pos.text.split()))
keys = list(filter(None, keys))

#  dict(name: link)
names = {}
for actions in html_data[1].find_all("a"):
    names[actions.text] = "https://markets.businessinsider.com/" + actions.get("href")
print(names)

# dict(name: add per year info -> str)
vals = []
for pos in html_data[1].find_all("td"):
    vals.append(" ".join(pos.text.split()))
vals = list(filter(None, vals))
