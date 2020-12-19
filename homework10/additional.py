from parser import html_data

#  just list of parameters
keys = []
for pos in html_data[1].find_all("th"):
    keys.append(" ".join(pos.text.split()))
keys = list(filter(None, keys))

# dict(name: link)
companies_link = {}
for link in html_data[1].find_all("a"):
    companies_link[link.text] = "https://markets.businessinsider.com/" + link.get(
        "href"
    )
