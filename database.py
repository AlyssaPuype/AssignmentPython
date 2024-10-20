import sqlite3

CREATE_USERS_TABLE = "CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT);"
INSERT_USER = "INSERT INTO users (name) VALUES(?);"
GET_ALL_USERS = "SELECT * FROM users;"
GET_USER_BY_NAME = "SELECT * FROM users WHERE name =?;"


def connect():
    return sqlite3.connect("run.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)

def add_user(connection, name):
    with connection:
        connection.execute(INSERT_USER,(name))

def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_user_by_name(connection, name):
    with connection:
        return connection.execute(GET_USER_BY_NAME, (name,)).fetchall()