import faker
import random
import sqlite3
import queries
from constants import NUMBER_TASKS, NUMBER_USERS, database, Statuses


def generate_fake_data(number_users, number_tasks):
    fake = faker.Faker()

    users = []
    tasks = []
    statuses = [(s.value,) for s in Statuses]

    for i in range(number_users):
        name = fake.name()
        email = fake.email()
        users.append((name, email))

    for i in range(number_tasks):
        text = fake.text()
        title = text[0:10]
        if i % 10 == 0:
            text = None
        tasks.append((title, text))

    return users, tasks, statuses


def prepare_data(users, tasks, statuses):
    prepared_tasks = []

    for title, descr in tasks:
        user_id = random.randint(1, len(users) - 2)
        status_id = random.randint(1, len(statuses))

        prepared_tasks.append((title, descr, status_id, user_id))

    return users, prepared_tasks, statuses


def insert_data_to_db(users, tasks, statuses):
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.executemany(queries.insert_user, users)
        cur.executemany(queries.insert_status, statuses)
        cur.executemany(queries.insert_task, tasks)
        con.commit()


if __name__ == "__main__":
    data = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    prepared_data = prepare_data(*data)
    insert_data_to_db(*prepared_data)
