from threading import Thread
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

    return [" ".join(i) for i in zip(vals[1::8], vals[7::8], vals[::8])]


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

    # company code
    code = str(parse_page(link).find_all("span", class_="price-section__category"))[
        53:-15
    ]

    # min, max stonks
    for elem in parse_page(link).find_all("script"):
        if not str(elem).find("high52weeks") == -1:
            stonk_info = " ".join(str(elem)[125:179].split()[1::2])

    # P/E
    colls = []
    for col in parse_page(link).find_all("div", class_="snapshot__data-item"):
        colls.append(" ".join(col.text.split()))

    return code + " " + colls[8][:5] + " " + stonk_info


url = "https://markets.businessinsider.com/index/components/s&p_500"
links = get_all_links(url)

i = 1
print(
    (get_info_from_main_page(url)[i] + " " + get_personal_add_info(links[i])).split()[
        1:
    ]
)

# задача 1. вывести все в потоках
# закрытая стоимость[0], % годовая[2], наименования, код[-4], P/E[-3], max stonks[-2], min stonks[-1]


class MyThread(Thread):
    """
    A threading example
    """

    result = []

    def __init__(self, name):
        """Thread initialization"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """thread start"""
        self.result.append(self.name)


def create_threads(n: int):
    """
    threads group creation
    """
    for i in range(n):
        my_thread = MyThread(i)
        my_thread.start()
    # print(my_thread.result)


create_threads(500)
