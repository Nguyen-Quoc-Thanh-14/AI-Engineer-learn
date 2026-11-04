# coding: utf-8
# Bài PA01.02 — Tài liệu có thể thực thi độc lập
import csv,io,json
rows=list(csv.DictReader(io.StringIO('name,qty\nAn,2\n')))
assert json.loads(json.dumps(rows))[0]['name']=='An'
