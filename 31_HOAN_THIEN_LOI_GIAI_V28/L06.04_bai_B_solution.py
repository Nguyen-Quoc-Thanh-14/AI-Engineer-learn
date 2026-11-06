import asyncio
async def main():
    q=asyncio.Queue(maxsize=5);seen=[]
    async def producer():
        for n in range(100): await q.put(n)
        await q.put(None)
    async def consumer():
        while True:
            x=await q.get()
            try:
                if x is None:return
                seen.append(x)
            finally:q.task_done()
    await asyncio.wait_for(asyncio.gather(producer(),consumer()),3)
    assert sorted(seen)==list(range(100))
asyncio.run(main())
