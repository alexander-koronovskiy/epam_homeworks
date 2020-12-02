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
import time

import requests


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Время выполнения: {} секунд.".format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    webpage = requests.get(url)
    return webpage.text


def count_dots_on_i(url: str) -> int:
    count = 0
    webpage = fetch_webpage(url)
    for i in str(webpage):
        if i == "i":
            count += 1
    return count
