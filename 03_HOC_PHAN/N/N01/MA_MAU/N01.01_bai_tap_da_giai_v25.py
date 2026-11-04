# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import re

def parse_age(value: str) -> int:
    if not isinstance(value, str):
        raise TypeError('age phải là chuỗi')
    value = value.strip()
    if not re.fullmatch(r'[0-9]{1,3}', value, flags=re.ASCII):
        raise ValueError('chỉ nhận số nguyên ASCII có 1–3 chữ số')
    age = int(value)
    if age > 130:
        raise ValueError('age ngoài miền [0,130]')
    return age

def check():
    assert parse_age(' 25 ') == 25
    assert parse_age('0') == 0 and parse_age('130') == 130
    for value in ('131', '12; DROP TABLE users', '-1', ''):
        try: parse_age(value)
        except ValueError: pass
        else: raise AssertionError('phải từ chối '+value)
    try: parse_age(True)
    except TypeError: pass
    else: raise AssertionError('bool không phải str')

if __name__ == '__main__':
    check()
    print('OK N01.01')
