# coding: utf-8
# Bài M05.02 — Tài liệu có thể thực thi độc lập
import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE users(id INTEGER PRIMARY KEY)')
    db.execute('ALTER TABLE users ADD COLUMN active INTEGER DEFAULT 1')
    db.execute('INSERT INTO users(id) VALUES (3)')
    assert db.execute('SELECT active FROM users').fetchone()[0]==1
