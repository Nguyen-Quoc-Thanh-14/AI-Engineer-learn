# coding: utf-8
# Bài PA04.02 — Tài liệu có thể thực thi độc lập
def schedule_status(attempts,limit=3):return 'retry' if attempts<limit else 'failed'
assert schedule_status(1)=='retry'
assert schedule_status(3)=='failed'
