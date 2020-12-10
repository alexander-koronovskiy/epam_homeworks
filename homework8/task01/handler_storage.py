"""
Класс KeyValueStorage - обработчик словаря, хранимого в файле

- хранит все пары ключ-значение переданного файла +++
- реализован доступ к атрибутам +++
- реализован доступно в качестве коллекции +++

- производит обработку численных значений
- производит valueError обработку
- решен конфликт атрибутов
"""
from typing import Dict


class KeyValueStorage:
    def __init__(self, storage):
        self.storage = storage

    def __getitem__(self, item):
        return content_reader(self.storage)[item]

    def __getattr__(self, name):
        return content_reader(self.storage)[name]


def content_reader(file: str) -> Dict:
    stringList = {}
    with open(file) as f:
        for line in f:
            key, value = line[:-1].split("=")
            # check for not unique key
            # check for int value
            # attribute conflict solution
            stringList[key] = value
        return stringList


storage = KeyValueStorage("key_storage.txt")
print(storage["name"], storage.name)
