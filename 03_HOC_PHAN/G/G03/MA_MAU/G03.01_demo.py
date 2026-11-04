# coding: utf-8
# Bài G03.01 — Tài liệu có thể thực thi độc lập
import csv, io
s = io.StringIO(newline='')
csv.writer(s).writerow(['name', 'note'])
csv.writer(s).writerow(['Lan', 'a,b'])
s.seek(0)
rows = list(csv.reader(s))
assert rows[1] == ['Lan', 'a,b']
