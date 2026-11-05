# coding: utf-8
# Bài PN02.02 — Tài liệu có thể thực thi độc lập
import torch
w=torch.nn.Parameter(torch.tensor(1.));loss=(w-2)**2
loss.backward();assert w.grad.item()==-2
