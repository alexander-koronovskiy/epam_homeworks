"""
Напишите функцию, которая принимает URL-адрес в качестве входных данных
и посчитайте, сколько букв `i` присутствует в HTML по этому URL.
Напишите тест, который проверяет, что ваша функция работает.
Тест должен использовать Mock вместо реальных сетевых взаимодействий.
Вы можете использовать urlopen * или любые другие сетевые библиотеки.
В случае какой-либо сетевой ошибки поднимите ValueError ("Unreachable {url})".
задача готова, если выполнены следующие условия:
  - функция создана
  - функция правильно отформатирована
  - функция имеет положительные и отрицательные тесты
"""
import requests
from bs4 import BeautifulSoup

url = "https://python-scripts.com/file-exists"
count = 0
require_symbol = "i"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
for quotes in soup.find_all("p"):
    # print(quotes.text)
    for symbol in quotes.text:
        if symbol == require_symbol:
            count += 1
print(count)
