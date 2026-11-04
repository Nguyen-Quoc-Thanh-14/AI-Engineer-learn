# coding: utf-8
# Bài PL02.01 — Tài liệu có thể thực thi độc lập
import torch
net=torch.nn.Sequential(torch.nn.Linear(2,4),torch.nn.ReLU(),torch.nn.Linear(4,1))
assert net(torch.ones(3,2)).shape==(3,1)
