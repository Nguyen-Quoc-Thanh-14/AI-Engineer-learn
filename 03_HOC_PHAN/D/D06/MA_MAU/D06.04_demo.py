# coding: utf-8
# Bài D06.04 — Tài liệu có thể thực thi độc lập
def length(value: str | None) -> int:
    if value is None: return 0
    return len(value)
assert length(None)==0 and length('abc')==3
