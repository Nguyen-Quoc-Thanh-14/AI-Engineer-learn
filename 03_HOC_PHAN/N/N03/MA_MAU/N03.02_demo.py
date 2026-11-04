# coding: utf-8
# Bài N03.02 — Tài liệu có thể thực thi độc lập
def bounded_retry(fn, limit=3):
    for i in range(limit):
        try: return fn()
        except TimeoutError:
            if i+1==limit: raise
attempts=[0]
def flaky():
    attempts[0]+=1
    if attempts[0]<2: raise TimeoutError()
    return 'ok'
assert bounded_retry(flaky)=='ok'
