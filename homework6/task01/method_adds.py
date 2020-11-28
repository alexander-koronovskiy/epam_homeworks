"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:

get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса

Имя декоратора и методов неизменно
"""


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print("[*] Время выполнения: {} секунд.".format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests

    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage("https://google.com")
# print(webpage)
