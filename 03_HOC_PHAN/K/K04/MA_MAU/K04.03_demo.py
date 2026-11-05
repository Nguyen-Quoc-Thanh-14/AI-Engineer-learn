# coding: utf-8
# Bài K04.03 — Tài liệu có thể thực thi độc lập
def total_a(xs):
    result=0
    for x in xs: result+=x
    return result
assert total_a([1,2,3])==sum([1,2,3])
