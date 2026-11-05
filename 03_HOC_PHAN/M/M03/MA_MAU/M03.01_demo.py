# coding: utf-8
# Bài M03.01 — Tài liệu có thể thực thi độc lập
import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('PRAGMA foreign_keys=ON')
    db.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)')
    db.execute('INSERT INTO users VALUES (?,?)',(1,'An'))
    assert db.execute('SELECT name FROM users WHERE id=1').fetchone()==('An',)
