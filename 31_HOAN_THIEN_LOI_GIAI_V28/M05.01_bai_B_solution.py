import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('PRAGMA foreign_keys = ON')
    db.executescript('CREATE TABLE user(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE); CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES user(id));')
    db.execute('INSERT INTO user(email) VALUES (?)',('a@example.test',))
    db.execute('INSERT INTO orders(user_id) VALUES (1)')
    try:
        db.execute('INSERT INTO user(email) VALUES (?)',('a@example.test',))
    except sqlite3.IntegrityError:pass
    else:raise AssertionError('unique violation accepted')
# This demonstrates DB constraints; ORM mapping itself requires a separate SQLAlchemy project.
