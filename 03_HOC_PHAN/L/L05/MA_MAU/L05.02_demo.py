# coding: utf-8
# Bài L05.02 — Tài liệu có thể thực thi độc lập
import asyncio
async def main():
    async with asyncio.TaskGroup() as tg:
        a=tg.create_task(asyncio.sleep(0,result=3))
    assert a.result()==3
asyncio.run(main())
