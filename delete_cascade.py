import sqlite3
from constants import database


# an example how to delete record in parent and child tables
# the main thing is PRAGMA instruction
def delete_user(id):
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=ON;")
        cur.execute(f"DELETE FROM users WHERE id={id}")
        con.commit()


if __name__ == "__main__":
    delete_user(2)
