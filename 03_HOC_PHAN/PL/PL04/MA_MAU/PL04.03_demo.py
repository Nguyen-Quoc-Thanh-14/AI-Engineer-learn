# coding: utf-8
# Bài PL04.03 — Tài liệu có thể thực thi độc lập
import torch
m=torch.nn.Linear(1,1);m.eval()
with torch.no_grad(): out=m(torch.ones(1,1))
assert out.shape==(1,1)
