# coding: utf-8
# Bài L02.03 — Tài liệu có thể thực thi độc lập
import threading
lock1=threading.Lock(); lock2=threading.Lock()
with lock1:
    with lock2:
        value=42
assert value==42
