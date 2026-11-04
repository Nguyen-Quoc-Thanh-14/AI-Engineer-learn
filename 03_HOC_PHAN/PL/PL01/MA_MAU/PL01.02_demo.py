# coding: utf-8
# Bài PL01.02 — Tài liệu có thể thực thi độc lập
import torch
x=torch.tensor(3.,requires_grad=True)
y=x*x;y.backward()
assert x.grad.item()==6
