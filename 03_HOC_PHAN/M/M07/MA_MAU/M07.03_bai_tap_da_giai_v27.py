# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import sqlite3
c=sqlite3.connect(':memory:');c.execute('CREATE TABLE acc(id INT PRIMARY KEY, balance INT CHECK(balance>=0))')
c.executemany('INSERT INTO acc VALUES(?,?)',[(1,100),(2,50)])
def transfer(src,dst,amount):
    if amount<=0:raise ValueError
    with c:
        n=c.execute('UPDATE acc SET balance=balance-? WHERE id=? AND balance>=?',(amount,src,amount)).rowcount
        if n!=1:raise ValueError('insufficient')
        n=c.execute('UPDATE acc SET balance=balance+? WHERE id=?',(amount,dst)).rowcount
        if n!=1:raise ValueError('missing receiver')
transfer(1,2,20)
assert c.execute('SELECT SUM(balance) FROM acc').fetchone()[0]==150
try:transfer(1,9,10)
except ValueError:pass
else:raise AssertionError
assert c.execute('SELECT balance FROM acc WHERE id=1').fetchone()[0]==80
c.close();print('PASS M07.03')
