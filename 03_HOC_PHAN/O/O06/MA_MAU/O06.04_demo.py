# coding: utf-8
# Bài O06.04 — Tài liệu có thể thực thi độc lập
def area(w,h):
    """Return rectangle area for nonnegative dimensions."""
    if w<0 or h<0: raise ValueError()
    return w*h
assert area(2,3)==6
