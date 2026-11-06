# coding: utf-8
# Bài O03.03 — Tài liệu có thể thực thi độc lập
def format_user(name, *, upper=False):
    return name.upper() if upper else name
assert format_user('An')=='An'
assert format_user('An',upper=True)=='AN'
