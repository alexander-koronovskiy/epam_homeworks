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


class MyThread(Thread):
    """
    A threading example
    """

    result = []

    def __init__(self, name, url):
        """Thread initialization"""
        Thread.__init__(self)
        self.i = int(name)
        self.url = url
        self.links = get_all_links(url)

    def run(self):
        """thread start"""
        self.result.append(
            get_info_from_main_page(self.url)[self.i]
            + " "
            + get_personal_add_info(self.links[self.i])
        )


def create_threads(n: int):
    """
    threads group creation
    """
    for i in range(n):
        my_thread = MyThread(i, url)
        my_thread.start()
    return my_thread.result


# распределить тут,
recordings = []
for i in range(1, 2):
    url = "https://markets.businessinsider.com/index/components/s&p_500?p=" + str(i)
    links = get_all_links(url)
    link_quantity = len(links)
    recordings.extend(create_threads(link_quantity))


# код[-4], наименования[4:-4],стоимость[0], % годовая[3],  P/E[-3], max stonks[-2], min stonks[-1]
for rec in recordings:
    data_elem = rec.split()
    print(
        {
            "code": data_elem[-4],
            "name": " ".join(data_elem[4:-4]),
            "per-year-cost": data_elem[0],
            "p/e": data_elem[3],
            "max-stonk": data_elem[-2],
            "min-stonk": data_elem[-1],
        }
    )

# обертка времени выполения (в тестах)
# обертка в словарь
