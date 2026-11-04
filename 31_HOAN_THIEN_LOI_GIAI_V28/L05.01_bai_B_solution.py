import asyncio
async def work(events):
    events.append('open')
    try: await asyncio.sleep(60)
    finally: events.append('close')
async def main():
    events=[];task=asyncio.create_task(work(events))
    await asyncio.sleep(0);task.cancel()
    try: await task
    except asyncio.CancelledError: pass
    assert events==['open','close']
asyncio.run(main())
