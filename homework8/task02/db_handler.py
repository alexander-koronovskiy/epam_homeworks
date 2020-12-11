"""
Написать класс-оболочку TableData для таблицы базы данных,
которая при инициализации с именем базы данных и таблицей реализует протокол коллекции.

Избегать считывания всей таблицы в память.
При итерации по записям начните читать первую запись, затем переходите к следующей,
пока записи не будут исчерпаны.

При написании тестов не всегда необходимо полностью имитировать вызовы базы данных.
Использовать предоставленный файл example.sqlite в качестве файла базы данных.
"""

import sqlite3 as lite
from typing import Generator

# реализовать доступ к элементу
# реализовать протокол __len__

# спросить про декорирование
# спросить про mock-тестирование


class TableHandle:
    def __init__(self, base, table):
        self.base = base
        self.table = table

    def __getitem__(self, row):
        return sql_reader(self.base, row, self.table)

    def __getattr__(self, row):
        return sql_reader(self.base, row, self.table)


def sql_reader(database: str, row: str, table: str) -> Generator:
    con = lite.connect(database)
    with con:
        cur = con.cursor()

        cur.execute("SELECT {} FROM {}".format(row, table))

        rows = cur.fetchall()

        for row in rows:
            yield row[0]


tab = TableHandle("example.sqlite", "presidents")
for i in tab["name"]:
    print(i)

for i in tab.country:
    print(i)
