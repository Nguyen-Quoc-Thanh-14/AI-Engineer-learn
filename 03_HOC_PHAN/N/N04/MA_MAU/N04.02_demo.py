# coding: utf-8
# Bài N04.02 — Tài liệu có thể thực thi độc lập
def can_edit(user_id, owner_id, is_admin=False):
    return user_id == owner_id or is_admin
assert can_edit('a','a')
assert not can_edit('a','b')
assert can_edit('a','b',True)
