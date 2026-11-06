# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import asyncio
async def f(x):
    await asyncio.sleep(0)
    return x
async def main():
    sem=asyncio.Semaphore(2)
    async def run(x):
        async with sem:return await f(x)
    return await asyncio.gather(*(run(i) for i in range(4)))
assert asyncio.run(main())==[0,1,2,3]
