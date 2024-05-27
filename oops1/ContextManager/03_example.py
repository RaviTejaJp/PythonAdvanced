import sqlite3
from contextlib import contextmanager


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()


@contextmanager
def open_database(db_name):
    connection = sqlite3.connect(db_name)
    try:
        yield connection
    finally:
        connection.close()


# Using the database context manager
with open_database("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name")
    results = cursor.fetchall()

with DatabaseConnection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM table_name")
    results = cursor.fetchall()
