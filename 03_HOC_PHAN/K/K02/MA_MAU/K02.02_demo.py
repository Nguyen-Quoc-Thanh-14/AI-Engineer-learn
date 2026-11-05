# coding: utf-8
# Bài K02.02 — Tài liệu có thể thực thi độc lập
import tracemalloc
tracemalloc.start()
before,_=tracemalloc.get_traced_memory()
data=[str(i) for i in range(200)]
after,_=tracemalloc.get_traced_memory()
assert after>=before
tracemalloc.stop()
