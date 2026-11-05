import asyncio
async def main():
    q=asyncio.Queue(maxsize=2);seen=[]
    async def producer():
        for n in range(30): await q.put(n)
        await q.put(None)
    async def consumer():
        while True:
            value=await q.get()
            try:
                if value is None: return
                seen.append(value)
            finally:q.task_done()
    await asyncio.wait_for(asyncio.gather(producer(),consumer()),timeout=2)
    await q.join()
    assert seen==list(range(30)) and q.maxsize==2
asyncio.run(main())
