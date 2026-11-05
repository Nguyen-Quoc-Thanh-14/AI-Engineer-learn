# coding: utf-8
# Bài PR02.04 — Tài liệu có thể thực thi độc lập
from packaging.tags import sys_tags
first=next(iter(sys_tags()))
assert first.interpreter
