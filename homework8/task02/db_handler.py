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


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class TableHandle:
    def __init__(self, base, table):
        self.base = base
        self.table = table

    def _get_connection(self):
        con = lite.connect(self.base)
        con.row_factory = lite.Row  # or use dict_factory
        return con

    def __len__(self):
        with self._get_connection() as con:
            cur = con.cursor()
            return cur.execute(f"SELECT COUNT(*) AS c FROM {self.table}").fetchone()[
                "c"
            ]

    def __getitem__(self, row):
        with self._get_connection() as con:
            cur = con.cursor()
            return cur.execute(
                f"SELECT * FROM {self.table} WHERE name = '{row}'"
            ).fetchone()

    def __iter__(self):
        with self._get_connection() as con:
            cur = con.cursor()
            for item in cur.execute(f"SELECT * FROM {self.table}"):
                yield item

    def __contains__(self, item):
        with self._get_connection() as con:
            cur = con.cursor()
            return cur.execute(
                f"SELECT * FROM {self.table} WHERE name = '{item}' LIMIT 1"
            ).fetchall()


presidents = TableHandle("example.sqlite", "presidents")
print("len: ", len(presidents))
print("name: ", dict(presidents["Yeltsin"]))
for president in presidents:
    print(president["name"])
print("Putin" in presidents)
