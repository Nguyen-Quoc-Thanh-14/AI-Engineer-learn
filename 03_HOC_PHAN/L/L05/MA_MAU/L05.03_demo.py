# coding: utf-8
# Bài L05.03 — Tài liệu có thể thực thi độc lập
import asyncio
async def main():
    q=asyncio.Queue(maxsize=1)
    await q.put('x')
    assert q.full()
    assert await q.get()=='x';q.task_done();await q.join()
asyncio.run(main())
