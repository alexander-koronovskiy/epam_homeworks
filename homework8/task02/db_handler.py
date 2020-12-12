"""
len(presidents) will give current amount of rows in presidents table in database
presidents['Yeltsin'] should return single data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
    for president in presidents:
        print(president['name'])
"""

import sqlite3 as lite
from typing import Callable, Generator, List

# реализовать доступ к элементу +++
# реализовать протокол __len__
# спросить про mock-тестирование


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class TableHandle:
    def __init__(self, base, table):
        self.base = base
        self.table = table

    def _with_cursor(self, fn: Callable):
        con = lite.connect(self.base)
        con.row_factory = lite.Row  # or use dict_factory
        with con:
            cur = con.cursor()
            return fn(cur)

    def __len__(self):
        return self._with_cursor(
            lambda cur: cur.execute(
                f"SELECT COUNT(*) AS c FROM {self.table}"
            ).fetchone()
        )["c"]

    def __getitem__(self, row):
        return self._with_cursor(
            lambda cur: cur.execute(
                f"SELECT * FROM {self.table} WHERE name = '{row}'"
            ).fetchone()
        )

    def __iter__(self):
        return iter(
            self._with_cursor(lambda cur: cur.execute(f"SELECT * FROM {self.table}"))
        )

    def __getattr__(self, row):
        return elem_reader(self.base, row, self.table)


def row_reader(database: str, row: str, table: str) -> Generator:
    con = lite.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("SELECT {} FROM {}".format(row, table))
        rows = cur.fetchall()
        for row in rows:
            yield row[0]


# # new 'name' query access realisation
def elem_reader(database: str, row: str, table: str) -> List:
    con = lite.connect(database)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM {} WHERE name = '{}'".format(table, row))
        rows = cur.fetchall()
        return rows


presidents = TableHandle("example.sqlite", "presidents")
print("len: ", len(presidents))
print("name: ", dict(presidents["Yeltsin"]))
for president in presidents:
    print(president["name"])
