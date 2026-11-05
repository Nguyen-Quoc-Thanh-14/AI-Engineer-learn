# coding: utf-8
# Bài F05.01 — Tài liệu có thể thực thi độc lập
import importlib, math
m1 = importlib.import_module('math')
m2 = importlib.import_module('math')
assert m1 is m2
