"""
Класс Storage handler

- хранит все значения переданного файла
- производит обработку численных значений
- содержимое доступно в качестве коллекции
- реализован доступ к атрибутам содержимого
"""

from task01.reader import word_stream


class StorageHandler:
    def __init__(self, storage):
        self.storage = storage


content = word_stream("key_storage.txt", encoding="utf-8")
for word in content:
    print(word)
