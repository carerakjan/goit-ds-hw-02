import queries
import pandas
from sqlite3 import connect
from constants import database, Statuses


def print_data(head: str, data, columns=None):
    data_frame = pandas.DataFrame(data=data, columns=columns)
    if head:
        h = " ".join(head.split("_"))
        print(f"--- {h.upper()} ---", end="\n\n")
    print(data_frame, end="\n\n")


def select_tasks_by_user(uid):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_tasks_by_user, uid)
        print_data(
            head="select_tasks_by_user",
            data=cur.fetchall(),
            columns=("id", "title", "descr", "status", "user"),
        )
        cur.close()


def select_tasks_by_status(status):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_tasks_by_status, status)
        print_data(
            head="select_tasks_by_status",
            data=cur.fetchall(),
            columns=("id", "title", "descr", "status", "user"),
        )
        cur.close()


def update_task_status(data):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.update_task_status, data)
        con.commit()


def select_users_without_tasks():
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_users_without_tasks)
        print_data(
            head="select_users_without_tasks",
            data=cur.fetchall(),
            columns=("id", "name", "email"),
        )
        cur.close()


def select_tasks_with_status_except(status):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_tasks_with_status_except, status)
        print_data(
            head="select_tasks_with_status_except",
            data=cur.fetchall(),
            columns=("id", "title", "descr", "status", "user"),
        )
        cur.close()


def delele_task_by_id(tid):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.delele_task_by_id, tid)
        cur.close()


def select_users_by_email_like(email):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_users_by_email_like, (f"%{email}%",))
        print_data(
            head="select_users_by_email_like",
            data=cur.fetchall(),
            columns=("id", "name", "email"),
        )
        cur.close()


def update_user_name(data):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.update_user_name, data)
        con.commit()


def count_of_tasks_by_status():
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.count_of_tasks_by_status)
        print_data(
            head="count_of_tasks_by_status",
            data=cur.fetchall(),
            columns=("total_tasks", "status"),
        )
        cur.close()


def select_tasks_by_user_email_domain(domain):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_tasks_by_user_email_domain, (f"%@{domain}",))
        print_data(
            head="select_tasks_by_user_email_domain",
            data=cur.fetchall(),
            columns=("title", "descr", "name", "email"),
        )
        cur.close()


def select_tasks_without_desc():
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_tasks_without_desc)
        print_data(
            head="select_tasks_without_desc",
            data=cur.fetchall(),
            columns=("id", "title", "descr", "status", "user"),
        )
        cur.close()


def select_tasks_and_users_by_status(status):
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.select_tasks_and_users_by_status, status)
        print_data(
            head="select_tasks_and_users_by_status",
            data=cur.fetchall(),
            columns=("task_title", "status", "user"),
        )
        cur.close()


def count_of_user_tasks():
    with connect(database) as con:
        cur = con.cursor()
        cur.execute(queries.count_of_user_tasks)
        print_data(
            head="count_of_user_tasks",
            data=cur.fetchall(),
            columns=("total_tasks", "user"),
        )
        cur.close()


if __name__ == "__main__":
    select_tasks_by_user((1,))
    select_tasks_by_status((Statuses.NEW.value,))
    update_task_status((Statuses.COMPLETED.value, 1))
    select_users_without_tasks()
    select_tasks_by_status((Statuses.NEW.value,))
    select_tasks_with_status_except((Statuses.COMPLETED.value,))
    delele_task_by_id((3,))
    select_users_by_email_like(".com")
    update_user_name(("John Wick", 2))
    count_of_tasks_by_status()
    select_tasks_by_user_email_domain("example.com")
    select_tasks_without_desc()
    select_tasks_and_users_by_status((Statuses.IN_PROGRESS.value,))
    count_of_user_tasks()
