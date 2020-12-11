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


def sql_reader(database: str) -> Generator:
    con = lite.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("SELECT name FROM presidents")
        rows = cur.fetchall()

        for row in rows:
            yield row


for i in sql_reader("example.sqlite"):
    print(i)
