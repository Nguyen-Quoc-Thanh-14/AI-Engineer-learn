# coding: utf-8
# Bài N05.04 — Tài liệu có thể thực thi độc lập
risks=[('data_leak',5,3),('typo',1,2)]
prioritized=sorted(risks,key=lambda x:x[1]*x[2],reverse=True)
assert prioritized[0][0]=='data_leak'
