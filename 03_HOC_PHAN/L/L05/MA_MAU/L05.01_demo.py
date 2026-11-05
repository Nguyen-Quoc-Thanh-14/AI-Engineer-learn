# coding: utf-8
# Bài L05.01 — Tài liệu có thể thực thi độc lập
import asyncio
async def run():
    try:
        async with asyncio.timeout(.001): await asyncio.sleep(1)
    except TimeoutError: return True
assert asyncio.run(run())
