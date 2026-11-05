# coding: utf-8
# Bài PW04.01 — Tài liệu có thể thực thi độc lập
import asyncio
async def fetch():await asyncio.sleep(0);return 1
assert asyncio.run(fetch())==1
