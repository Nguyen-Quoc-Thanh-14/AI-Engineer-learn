# coding: utf-8
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def fetch_record(record_id):
    sleep(0.001)
    return {'id': record_id, 'value': record_id * 2}

def run_jobs(items):
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(fetch_record, item) for item in items]
        return [future.result(timeout=2) for future in futures]

if __name__ == '__main__':
    assert run_jobs([1, 2, 3]) == [
        {'id': 1, 'value': 2}, {'id': 2, 'value': 4}, {'id': 3, 'value': 6}]
    assert run_jobs([]) == []
    assert run_jobs([5])[0]['value'] == 10
    print('PASS L03.01')
