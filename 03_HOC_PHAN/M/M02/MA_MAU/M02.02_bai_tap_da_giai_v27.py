# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import random
def retry_get(request, *, max_attempts=4, seed=7):
    rng=random.Random(seed); delays=[]
    for attempt in range(max_attempts):
        status,body=request(attempt)
        if status==200:return body,delays
        if status not in {429,503}:raise RuntimeError(f'unretryable {status}')
        if attempt==max_attempts-1:break
        delays.append(min(2**attempt,4)+rng.random()*.1)
    raise TimeoutError('exhausted retry budget')
assert retry_get(lambda n:(503,None) if n==0 else (200,'ok'))[0]=='ok'
assert retry_get(lambda n:(200,'x'))[1]==[]
try:retry_get(lambda n:(400,None))
except RuntimeError:pass
else:raise AssertionError
print('PASS M02.02')
