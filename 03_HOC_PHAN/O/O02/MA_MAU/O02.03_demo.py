# coding: utf-8
# Bài O02.03 — Tài liệu có thể thực thi độc lập
def bump_patch(v):
    major,minor,patch=map(int,v.split('.'))
    return f'{major}.{minor}.{patch+1}'
assert bump_patch('1.2.3')=='1.2.4'
