# coding: utf-8
# Bài M03.03 — Tài liệu có thể thực thi độc lập
import sqlite3
with sqlite3.connect(':memory:') as db:
    db.execute('CREATE TABLE t(name TEXT)')
    db.executemany('INSERT INTO t VALUES (?)',[('An',),('Binh',)])
    bad="' OR 1=1 --"
    assert db.execute('SELECT * FROM t WHERE name=?',(bad,)).fetchall()==[]
