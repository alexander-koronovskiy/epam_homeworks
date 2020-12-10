"""
Класс KeyValueStorage - обработчик словаря, хранимого в файле

- хранит все пары ключ-значение переданного файла +++
- производит обработку численных значений
- содержимое доступно в качестве коллекции
- реализован доступ к атрибутам содержимого

- производит valueError обработку
- конфликт атрибутов ???
"""

from task01.reader import content_reader


class KeyValueStorage:
    def __init__(self, storage):
        self.storage = storage

    def all(self):
        return content_reader(self.storage)


storage = KeyValueStorage("key_storage.txt")
print(storage.all())
