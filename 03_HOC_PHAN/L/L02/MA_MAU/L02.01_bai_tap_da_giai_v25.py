# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

class Counter:
    def __init__(self):
        self._value = 0
        self._lock = Lock()

    def increment(self):
        with self._lock:
            self._value += 1

    @property
    def value(self):
        with self._lock:
            return self._value

def run_workers(workers: int, times: int) -> int:
    if type(workers) is not int or type(times) is not int or workers < 1 or times < 0:
        raise ValueError('workers >=1 và times >=0')
    counter = Counter()
    def job():
        for _ in range(times):
            counter.increment()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(lambda _: job(), range(workers)))
    return counter.value

def check():
    assert run_workers(4, 500) == 2000
    assert run_workers(1, 0) == 0
    try: run_workers(0, 2)
    except ValueError: pass
    else: raise AssertionError('workers phải dương')

if __name__ == '__main__':
    check()
    print('OK L02.01')
