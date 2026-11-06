# coding: utf-8
# Bài PV02.03 — Tài liệu có thể thực thi độc lập
a=['cat','dog','dog'];b=['cat','cat','dog']
assert sum(x==y for x,y in zip(a,b))/len(a)==2/3
