# coding: utf-8
# Bài PL03.02 — Tài liệu có thể thực thi độc lập
import torch
q=torch.ones(1,2,4);k=q.clone();v=q.clone()
o=torch.nn.functional.scaled_dot_product_attention(q,k,v)
assert o.shape==q.shape
