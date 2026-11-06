# coding: utf-8
# Bài PL04.02 — Tài liệu có thể thực thi độc lập
batch_size=8;world_size=4;accumulation=2
global_batch=batch_size*world_size*accumulation
assert global_batch==64
