# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import sqlite3
c=sqlite3.connect(':memory:')
c.executescript('CREATE TABLE users(id INT PRIMARY KEY); CREATE TABLE orders(id INT PRIMARY KEY,uid INT);'
'INSERT INTO users VALUES(1),(2); INSERT INTO orders VALUES(9,1),(10,1);')
rows=c.execute('SELECT u.id,COUNT(*),COUNT(o.id) FROM users u LEFT JOIN orders o ON o.uid=u.id GROUP BY u.id ORDER BY u.id').fetchall()
assert rows==[(1,2,2),(2,1,0)]
assert rows[1][1]!=rows[1][2]
assert len(rows)==2
c.close();print('PASS M03.02')
