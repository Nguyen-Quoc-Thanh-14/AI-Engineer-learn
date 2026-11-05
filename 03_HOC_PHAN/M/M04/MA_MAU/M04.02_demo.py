# coding: utf-8
# Bài M04.02 — Tài liệu có thể thực thi độc lập
from contextlib import closing
import sqlite3
with closing(sqlite3.connect(':memory:')) as db:
    assert db.execute('SELECT 1').fetchone()[0]==1
