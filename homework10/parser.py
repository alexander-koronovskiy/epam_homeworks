import requests
from bs4 import BeautifulSoup


def parse_page(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


url = "https://markets.businessinsider.com/index/components/s&p_500"
html_data = parse_page(url).find_all("table")

# dict(name: costs, per year info -> str)
vals = []
for pos in html_data[1].find_all("td"):
    vals.append(" ".join(pos.text.split()))
vals = list(filter(None, vals))

# for all companies name, per year dynamics, last price
main_table_info = [" ".join(i) for i in zip(vals[::8], vals[1::8], vals[7::8])]


# :links
src_pages = [
    "https://markets.businessinsider.com/" + link.get("href")
    for link in html_data[1].find_all("a")
]

# looping info P/E, min and max per year in threads
explore_link = src_pages[0]

# P/E
colls = []
for col in parse_page(explore_link).find_all("div", class_="snapshot__data-item"):
    colls.append(" ".join(col.text.split()))
pe0 = colls[8]

# 1 вытащить js данные, добавить к основам
# parse_page(explore_link).find_all("script")[28]

# 2 все склеить, проанализировать для одной строчки в потоке
print(main_table_info[0] + " " + pe0)
