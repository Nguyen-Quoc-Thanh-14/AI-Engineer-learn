# coding: utf-8
# Bài J02.03 — Tài liệu có thể thực thi độc lập
import copy
original=[[1],[2]]
shallow=copy.copy(original)
deep=copy.deepcopy(original)
original[0].append(3)
assert shallow[0]==[1,3]
assert deep[0]==[1]
