import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('PRAGMA foreign_keys = ON')
    db.execute('CREATE TABLE user(id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL)')
    db.execute('CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES user(id))')
    db.execute('INSERT INTO user VALUES (1, "a@example.test")')
    db.execute('INSERT INTO orders VALUES (100, 1)')
    try:db.execute('INSERT INTO orders VALUES (101, 999)')
    except sqlite3.IntegrityError:pass
    else:raise AssertionError('foreign key absent')
