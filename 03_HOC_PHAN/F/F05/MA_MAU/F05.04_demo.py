# coding: utf-8
# Bài F05.04 — Tài liệu có thể thực thi độc lập
import importlib, time
start = time.perf_counter()
mod = importlib.import_module('statistics')
elapsed = time.perf_counter() - start
assert elapsed >= 0 and mod.mean([1, 2, 3]) == 2
