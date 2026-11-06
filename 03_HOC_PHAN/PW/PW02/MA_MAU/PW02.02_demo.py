# coding: utf-8
# Bài PW02.02 — Tài liệu có thể thực thi độc lập
def can_read(user_id,owner_id):return user_id==owner_id
assert can_read(1,1) and not can_read(2,1)
