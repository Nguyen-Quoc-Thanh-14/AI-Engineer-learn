# coding: utf-8
# Bài J02.02 — Tài liệu có thể thực thi độc lập
fs=[lambda i=i: i*i for i in range(4)]
assert [f() for f in fs]==[0,1,4,9]
wrong=[lambda: i for i in range(3)]
assert [f() for f in wrong]==[2,2,2]
