# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import asyncio
async def boom(exc):
    raise exc
async def main():
    observed=[]
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(boom(ValueError('one')))
            tg.create_task(boom(ValueError('two')))
    except* ValueError as eg:
        observed.extend(str(x) for x in eg.exceptions)
    assert sorted(observed)==['one','two']
asyncio.run(main());print('PASS L05.02')
