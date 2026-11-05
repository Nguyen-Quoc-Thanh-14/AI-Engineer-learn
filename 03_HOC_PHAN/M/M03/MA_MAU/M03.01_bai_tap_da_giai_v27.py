# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import sqlite3
conn=sqlite3.connect(':memory:');conn.execute('PRAGMA foreign_keys=ON')
conn.execute('CREATE TABLE users(id INTEGER PRIMARY KEY)')
conn.execute('CREATE TABLE orders(id INTEGER PRIMARY KEY,user_id INTEGER REFERENCES users(id))')
conn.execute('INSERT INTO users VALUES(1)')
conn.execute('INSERT INTO orders VALUES(1,1)')
assert conn.execute('SELECT count(*) FROM orders').fetchone()[0]==1
try:conn.execute('INSERT INTO orders VALUES(2,999)')
except sqlite3.IntegrityError:pass
else:raise AssertionError
conn.close();print('PASS M03.01')
