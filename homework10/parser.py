from typing import List

import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


def get_info_from_main_page(url: str) -> List[str]:
    """
    returns info string for all companies
    name, last price, per year dynamics
    """
    html_data = parse_page(url).find_all("table")

    vals = []
    for pos in html_data[1].find_all("td"):
        vals.append(" ".join(pos.text.split()))
    vals = list(filter(None, vals))

    return [" ".join(i) for i in zip(vals[::8], vals[1::8], vals[7::8])]


def get_all_links(url: str) -> List[str]:
    """
    return list of companies links for information parse
    """
    html_data = parse_page(url).find_all("table")
    return [
        "https://markets.businessinsider.com/" + link.get("href")
        for link in html_data[1].find_all("a")
    ]


def get_personal_add_info(link: str) -> str:

    # словать из строки
    s = str(parse_page(link).find_all("script")[28])[125:180]

    # P/E
    colls = []
    for col in parse_page(link).find_all("div", class_="snapshot__data-item"):
        colls.append(" ".join(col.text.split()))
    return colls[8] + " ".join(s.split())


url = "https://markets.businessinsider.com/index/components/s&p_500"
links = get_all_links(url)

i = 3
print((get_info_from_main_page(url)[i] + " " + get_personal_add_info(links[i])).split())

# задача 1. вывести все в потоках

# задача 2. словари из значений:
# имя[0], закрытая текущая стоимость[1,2], процентная за год[4], p/e[5], max_profit[8 - 10], code[11]
