# coding: utf-8
from multiprocessing import Pipe, Process
import json

def worker(conn):
    try:
        for value in (2, 3):
            conn.send_bytes(json.dumps({'kind': 'square', 'value': value**2}).encode('utf-8'))
    finally:
        conn.close()

def receive_messages():
    parent, child = Pipe(duplex=False)
    proc = Process(target=worker, args=(child,))
    proc.start(); child.close()
    out = []
    try:
        for _ in range(2):
            if not parent.poll(3): raise TimeoutError('worker did not send')
            message = json.loads(parent.recv_bytes(maxlength=1024))
            if set(message) != {'kind', 'value'} or message['kind'] != 'square' or type(message['value']) is not int:
                raise ValueError('unexpected payload')
            out.append(message['value'])
    finally:
        parent.close()
        proc.join(timeout=3)
        if proc.is_alive(): proc.terminate(); proc.join()
    if proc.exitcode != 0: raise RuntimeError('worker failed')
    return out

if __name__ == '__main__':
    assert receive_messages() == [4, 9]
    assert json.loads(json.dumps({'kind': 'square', 'value': 4}))['value'] == 4
    try:
        unexpected = {'kind': 'delete', 'value': 4}
        if unexpected['kind'] != 'square': raise ValueError('schema')
    except ValueError: pass
    else: raise AssertionError
    print('PASS L03.03')
