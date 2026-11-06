# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import sqlite3
c=sqlite3.connect(':memory:')
c.execute('CREATE TABLE events(id INTEGER PRIMARY KEY,category TEXT)')
c.executemany('INSERT INTO events(category) VALUES(?)',[('x',)]*20+[('y',)]*20)
c.execute('CREATE INDEX idx_events_cat ON events(category)')
plan=' '.join(str(x) for x in c.execute('EXPLAIN QUERY PLAN SELECT * FROM events WHERE category=?',('x',)))
assert 'idx_events_cat' in plan
assert c.execute('SELECT COUNT(*) FROM events WHERE category=?',('x',)).fetchone()[0]==20
assert c.execute('SELECT COUNT(*) FROM events').fetchone()[0]==40
c.close();print('PASS M03.03')
