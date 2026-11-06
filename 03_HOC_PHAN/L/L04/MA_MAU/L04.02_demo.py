# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import asyncio
async def f(x):
    await asyncio.sleep(0)
    return x*2
async def main():
    return await asyncio.gather(f(1),f(2))
assert asyncio.run(main())==[2,4]
