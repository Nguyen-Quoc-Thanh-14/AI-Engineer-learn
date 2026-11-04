# coding: utf-8
# Bài M06.03 — Tài liệu có thể thực thi độc lập
import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE flags(id INTEGER PRIMARY KEY)')
    db.execute('INSERT INTO flags VALUES (1)')
    assert db.execute('SELECT COUNT(*) FROM flags').fetchone()[0]==1
