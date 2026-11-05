# coding: utf-8
# Bài O02.02 — Tài liệu có thể thực thi độc lập
from difflib import unified_diff
a=['value=1\n'];b=['value=2\n']
changes=list(unified_diff(a,b))
assert any('-value=1' in s for s in changes)
