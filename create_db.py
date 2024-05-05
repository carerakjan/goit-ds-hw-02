import sqlite3
from constants import database, sql_script


def create_db():
    with open(sql_script, "r") as f:
        sql = f.read()

    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
