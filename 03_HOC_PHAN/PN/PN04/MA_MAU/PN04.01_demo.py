# coding: utf-8
# Bài PN04.01 — Tài liệu có thể thực thi độc lập
text='abcdefghij';size=4;step=3
chunks=[text[i:i+size] for i in range(0,len(text),step)]
assert chunks[:2]==['abcd','defg']
