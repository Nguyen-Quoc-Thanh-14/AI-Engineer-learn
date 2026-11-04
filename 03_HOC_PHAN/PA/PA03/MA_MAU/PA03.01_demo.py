# coding: utf-8
# Bài PA03.01 — Tài liệu có thể thực thi độc lập
def extract():return [{'qty':2},{'qty':3}]
def transform(rows):return [r['qty'] for r in rows]
def load(values):return sum(values)
assert load(transform(extract()))==5
