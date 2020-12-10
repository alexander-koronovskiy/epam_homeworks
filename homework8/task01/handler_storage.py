"""
Класс KeyValueStorage - обработчик словаря, хранимого в файле

- хранит все пары ключ-значение переданного файла
- производит обработку численных значений
- содержимое доступно в качестве коллекции
- реализован доступ к атрибутам содержимого

- реализовать обработку valueError
- конфликт атрибутов ???
"""

from task01.reader import word_reader


# шаг 1. класс хранит слова +
# шаг 2. обработка пар ключ-значение
class KeyValueStorage:
    def __init__(self, storage):
        self.storage = storage

    def all(self):
        return word_reader(self.storage)


storage = KeyValueStorage("key_storage.txt")
print(storage.all())
