# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import sqlite3
con=sqlite3.connect(':memory:')
con.execute('create table t(id integer primary key, name text)')
con.execute('insert into t(name) values (?)',('An',))
assert con.execute('select name from t where id=?',(1,)).fetchone()==('An',)
con.close()
