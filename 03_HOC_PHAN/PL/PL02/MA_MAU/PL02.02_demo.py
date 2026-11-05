# coding: utf-8
# Bài PL02.02 — Tài liệu có thể thực thi độc lập
import torch
w=torch.nn.Parameter(torch.tensor(1.))
opt=torch.optim.SGD([w],lr=.1)
opt.zero_grad(); loss=(w-3)**2; loss.backward();opt.step()
assert w.item()>1
