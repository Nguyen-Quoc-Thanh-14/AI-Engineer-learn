# coding: utf-8
# Bài J07.02 — Tài liệu có thể thực thi độc lập
import gc
before=gc.isenabled()
assert isinstance(before,bool)
assert gc.collect()>=0
