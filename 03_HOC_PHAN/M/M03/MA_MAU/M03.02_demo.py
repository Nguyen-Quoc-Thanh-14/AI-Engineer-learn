# coding: utf-8
# Bài M03.02 — Tài liệu có thể thực thi độc lập
import sqlite3
with sqlite3.connect(':memory:') as db:
    db.executescript('CREATE TABLE items(cat TEXT, cost INT); INSERT INTO items VALUES ("a",2),("a",3),("b",4);')
    rows=db.execute('SELECT cat,SUM(cost) FROM items GROUP BY cat ORDER BY cat').fetchall()
    assert rows==[('a',5),('b',4)]
