# coding: utf-8
# Bài PN02.01 — Tài liệu có thể thực thi độc lập
import torch
q=torch.randn(1,2,4);k=q.clone();v=q.clone()
assert torch.nn.functional.scaled_dot_product_attention(q,k,v).shape==q.shape
