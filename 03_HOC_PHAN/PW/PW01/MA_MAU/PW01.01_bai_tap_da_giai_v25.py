# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from urllib.parse import urlsplit, parse_qs

def parse_http_url(raw: str):
    if not isinstance(raw, str):
        raise TypeError('URL phải là str')
    result = urlsplit(raw)
    if result.scheme not in ('http', 'https') or not result.hostname:
        raise ValueError('cần URL http(s) có host')
    if result.username is not None or result.password is not None:
        raise ValueError('không nhận credentials trong URL')
    return result.path or '/', parse_qs(result.query, keep_blank_values=True)

def check():
    path, query = parse_http_url('https://example.org/items?page=1&page=2')
    assert path == '/items' and query['page'] == ['1','2']
    assert parse_http_url('http://example.org')[0] == '/'
    try: parse_http_url('file:///etc/passwd')
    except ValueError: pass
    else: raise AssertionError('schema sai')
    try: parse_http_url(None)
    except TypeError: pass
    else: raise AssertionError('sai kiểu')

if __name__ == '__main__':
    check()
    print('OK PW01.01')
