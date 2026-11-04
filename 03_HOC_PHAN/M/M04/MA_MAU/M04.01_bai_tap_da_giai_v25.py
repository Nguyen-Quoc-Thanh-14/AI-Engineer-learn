# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import sqlite3

def create_db():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)')
    return db

def add_person(db, name):
    if not isinstance(name, str) or not name:
        raise ValueError('tên phải là chuỗi không rỗng')
    db.execute('INSERT INTO people(name) VALUES (?)', (name,))
    db.commit()

def find_person(db, name):
    return db.execute('SELECT name FROM people WHERE name = ?', (name,)).fetchall()

def check():
    with create_db() as db:
        add_person(db, 'Alice')
        add_person(db, "' OR 1=1 --")
        assert find_person(db, 'Alice') == [('Alice',)]
        assert find_person(db, "' OR 1=1 --") == [("' OR 1=1 --",)]
        assert find_person(db, 'nobody') == []
        try: add_person(db, '')
        except ValueError: pass
        else: raise AssertionError('tên rỗng')

if __name__ == '__main__':
    check()
    print('OK M04.01')
