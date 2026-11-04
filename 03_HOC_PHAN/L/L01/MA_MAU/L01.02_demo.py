# coding: utf-8
# Bài L01.02 — Tài liệu có thể thực thi độc lập
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as pool:
    assert list(pool.map(lambda x:x*x, [2,3]))==[4,9]
