# coding: utf-8
# Bài PR02.02 — Tài liệu có thể thực thi độc lập
from threading import Lock
lock=Lock()
with lock: value=1
assert value==1
