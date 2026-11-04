# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import torch

def gradient(values):
    x = torch.tensor(values, dtype=torch.float64, requires_grad=True)
    loss = (3 * x.square() + 2 * x).sum()
    loss.backward()
    return x.grad.detach().tolist()

def check():
    result = gradient([-1.0, 0.0, 2.0])
    assert torch.allclose(torch.tensor(result), torch.tensor([-4.0, 2.0, 14.0]))
    assert gradient([]) == []
    x = torch.tensor([1.0], requires_grad=True)
    (x * x).sum().backward()
    assert x.grad.item() == 2.0
    (x * x).sum().backward()
    assert x.grad.item() == 4.0  # tích lũy

if __name__ == '__main__':
    check()
    print('OK PL01.01', gradient([-1., 0., 2.]))
