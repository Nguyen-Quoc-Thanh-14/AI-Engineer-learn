# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import asyncio
async def task(name):
    await asyncio.sleep(0)
    return name
async def main():
    results=await asyncio.gather(task('A'),task('B'))
    assert results==['A','B']
    return results
print(asyncio.run(main()))
