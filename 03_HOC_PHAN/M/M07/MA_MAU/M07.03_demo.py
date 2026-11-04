# coding: utf-8
# Bài M07.03 — Tài liệu có thể thực thi độc lập
import sqlite3
db=sqlite3.connect(':memory:')
db.execute('CREATE TABLE balance(value INT)')
db.execute('INSERT INTO balance VALUES (100)')
db.commit()
try:
    db.execute('UPDATE balance SET value=0')
    raise ValueError()
except ValueError: db.rollback()
assert db.execute('SELECT value FROM balance').fetchone()[0]==100
db.close()
