import sqlite3

def get_con():
    return sqlite3.connect('db/bingo.db')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
