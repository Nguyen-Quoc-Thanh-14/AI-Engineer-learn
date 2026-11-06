# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import asyncio
async def lay_du_lieu():
    await asyncio.sleep(0)
    return 5
assert asyncio.run(lay_du_lieu())==5
