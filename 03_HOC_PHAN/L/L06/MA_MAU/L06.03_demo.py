# coding: utf-8
# Bài L06.03 — Tài liệu có thể thực thi độc lập
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as ex:
    assert list(ex.map(abs, [-1,-2]))==[1,2]
