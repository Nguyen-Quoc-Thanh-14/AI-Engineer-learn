# coding: utf-8
# Bài PR01.02 — Tài liệu có thể thực thi độc lập
import sys
x=[]
assert sys.getrefcount(x)>=2
