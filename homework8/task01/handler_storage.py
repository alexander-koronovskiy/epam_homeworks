"""
Класс KeyValueStorage - обработчик словаря, хранимого в файле

- хранит все пары ключ-значение переданного файла +++
- реализован доступ к атрибутам +++
- реализован доступ к элементам коллекции +++

- производит обработку численных значений
- производит valueError обработку
- решен конфликт приоритета значений атрибутов +++
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
        keys = []
        for line in f:
            # if line:
            key, value = line[:-1].split("=")

            # check for not unique key
            # check for int value

            # attribute value priority conflict solution
            if key not in keys:
                stringList[key] = value
            keys.append(key)

        return stringList


storage = KeyValueStorage("key_storage.txt")
print(content_reader("key_storage.txt"))
