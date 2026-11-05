# coding: utf-8
# Bài I07.01 — Tài liệu có thể thực thi độc lập
def sum_nonnegative(xs):
    total=0
    for i,x in enumerate(xs):
        total += x
        assert total == sum(xs[:i+1])
    return total
assert sum_nonnegative([2,-1,4])==5
