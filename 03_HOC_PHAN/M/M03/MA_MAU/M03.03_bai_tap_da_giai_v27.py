# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
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
