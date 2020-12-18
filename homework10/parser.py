"""
Получить информацию на сайте

- Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
- Код компании (справа от названия компании на странице компании)
- P/E компании (информация находится справа от графика на странице компании)
- Годовой рост/падение компании в процентах (основная таблица)
- Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)


"""

import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


url = "https://markets.businessinsider.com/index/components/s&p_500"
html_data = [row for row in parse_page(url).find_all("table")]


keys = []  # all keys for parse
for pos in html_data[1].find_all("th"):
    keys.append(" ".join(pos.text.split()))
keys = list(filter(None, keys))


names = []  # company names
for actions in html_data[1].find_all("a"):
    names.append(" ".join(actions.text.split()))
print(names)

# more code duplicates: prices, code, p/e, info per year - zip in dict, and transform
