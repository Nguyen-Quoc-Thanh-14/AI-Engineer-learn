# coding: utf-8
# Bài PW02.01 — Tài liệu có thể thực thi độc lập
from sqlalchemy import create_engine,text
engine=create_engine('sqlite+pysqlite:///:memory:')
with engine.connect() as conn:assert conn.execute(text('select 1')).scalar()==1
