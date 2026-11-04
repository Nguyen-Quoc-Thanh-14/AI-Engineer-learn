# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import sqlite3
c=sqlite3.connect(':memory:')
c.execute('create table t(x integer)')
try:
    with c:
        c.execute('insert into t values(1)')
        raise ValueError('rollback')
except ValueError:pass
assert c.execute('select count(*) from t').fetchone()[0]==0
c.close()
