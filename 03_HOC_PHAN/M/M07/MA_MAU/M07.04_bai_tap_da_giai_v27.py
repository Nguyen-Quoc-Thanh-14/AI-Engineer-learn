# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import sqlite3
c=sqlite3.connect(':memory:');c.execute('CREATE TABLE inbox(event_id TEXT PRIMARY KEY, payload TEXT NOT NULL)')
def ingest(event_id,payload):
    with c:
        return c.execute('INSERT OR IGNORE INTO inbox VALUES(?,?)',(event_id,payload)).rowcount
assert ingest('event1','A')==1
assert ingest('event1','A')==0
assert ingest('event0','B')==1
assert c.execute('SELECT COUNT(*) FROM inbox').fetchone()[0]==2
c.close();print('PASS M07.04')
