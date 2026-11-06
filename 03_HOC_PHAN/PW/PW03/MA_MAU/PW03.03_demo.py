# coding: utf-8
# Bài PW03.03 — Tài liệu có thể thực thi độc lập
import inspect
async def handler():return 200
assert inspect.iscoroutinefunction(handler)
