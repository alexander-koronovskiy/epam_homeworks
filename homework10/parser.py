from typing import List

import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


def get_info_from_main_page(url: str) -> List[str]:
    """
    returns info string for all companies
    about name, per year dynamics, last price
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

    print(str(parse_page(link).find_all("script")[28]))

    # P/E
    colls = []
    for col in parse_page(link).find_all("div", class_="snapshot__data-item"):
        colls.append(" ".join(col.text.split()))
    return colls[8] + " + info from js parse"


url = "https://markets.businessinsider.com/index/components/s&p_500"
links = get_all_links(url)
add_info = get_personal_add_info(links[0])

print(get_info_from_main_page(url)[0] + add_info)
