import sqlite3
from .GLOBAL import args

database = args.database
conn = sqlite3.connect(args.database, check_same_thread=False)
conn.execute('pragma foreign_keys=ON')


def dict_factory(cursor, row):
    """This is a function use to format the json when retrieve from the  mysql database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory
# Create tables if they do not exist

conn.execute('''CREATE TABLE if not exists user
(user_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_first_name TEXT NOT NULL,
user_last_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
is_admin BOOL NOT NULL DEFAULT FALSE);''')

conn.execute('''CREATE TABLE if not exists session
(sess_token TEXT NOT NULL PRIMARY KEY,
sess_date DATETIME NOT NULL,
user_id INTEGER NOT NULL,
FOREIGN KEY(user_id) REFERENCES user(user_id));''')
