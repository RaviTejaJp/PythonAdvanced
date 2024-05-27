from contextlib import contextmanager


@contextmanager
def simple_context_manager():
    print("Entering the context")
    yield  # this is a separator from the entry and exit code
    print("Exiting the context")


# Using the simple context manager
with simple_context_manager():
    print("Inside the context")

import sqlite3
from contextlib import contextmanager


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
