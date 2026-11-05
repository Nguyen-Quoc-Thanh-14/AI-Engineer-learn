# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from random import Random

def split_users(records: list[tuple[str, float]], seed: int = 42):
    if not isinstance(records, list):
        raise TypeError('records phải là list')
    users = sorted({user for user, _ in records})
    if len(users) < 3:
        raise ValueError('cần ít nhất 3 user độc lập')
    Random(seed).shuffle(users)
    train_n = max(1, len(users) * 6 // 10)
    validation_n = max(1, (len(users) - train_n) // 2)
    train_users = set(users[:train_n])
    validation_users = set(users[train_n:train_n+validation_n])
    test_users = set(users[train_n+validation_n:])
    return tuple(
        [row for row in records if row[0] in group]
        for group in (train_users, validation_users, test_users)
    )

def check():
    records = [(f'u{i}', float(i+j)) for i in range(10) for j in range(2)]
    a,b,c = split_users(records)
    users = [{x[0] for x in group} for group in (a,b,c)]
    assert all(users) and not (users[0] & users[1] | users[0] & users[2] | users[1] & users[2])
    assert len(a) + len(b) + len(c) == len(records)
    assert split_users(records) == (a,b,c)
    try: split_users([('u1',1.0)])
    except ValueError: pass
    else: raise AssertionError('ít group')

if __name__ == '__main__':
    check()
    print('OK PM01.02')
