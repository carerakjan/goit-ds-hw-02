from enum import Enum

NUMBER_USERS = 6

NUMBER_TASKS = 30

database = "todos.db"

sql_script = "tables.sql"


class Statuses(Enum):
    NEW = "new"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
