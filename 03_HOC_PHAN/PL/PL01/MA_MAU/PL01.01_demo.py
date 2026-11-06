# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import torch
x=torch.tensor([1.,2.,3.],requires_grad=True)
y=(x*x).sum()
y.backward()
assert torch.allclose(x.grad,torch.tensor([2.,4.,6.]))
print(x.grad.tolist())
