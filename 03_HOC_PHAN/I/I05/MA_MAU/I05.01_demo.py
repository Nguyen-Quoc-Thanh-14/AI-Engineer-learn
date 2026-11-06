# coding: utf-8
# Bài I05.01 — Tài liệu có thể thực thi độc lập
graph = {'A': {'B','C'}, 'B': {'C'}, 'C': set()}
assert graph['A'] == {'B','C'}
assert sum(map(len, graph.values())) == 3
