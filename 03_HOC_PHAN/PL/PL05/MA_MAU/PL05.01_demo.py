# coding: utf-8
# Bài PL05.01 — Tài liệu có thể thực thi độc lập
import torch
q=torch.randn(1,2,4);k=torch.randn(1,2,4);v=torch.randn(1,2,3)
weights=torch.softmax((q@k.transpose(-2,-1))/(4**.5),dim=-1)
assert (weights@v).shape==(1,2,3)
