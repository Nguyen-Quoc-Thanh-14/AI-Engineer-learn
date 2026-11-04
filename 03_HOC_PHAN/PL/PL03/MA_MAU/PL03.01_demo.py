# coding: utf-8
# Bài PL03.01 — Tài liệu có thể thực thi độc lập
import torch
conv=torch.nn.Conv2d(1,2,kernel_size=3,padding=1)
assert conv(torch.ones(1,1,8,8)).shape==(1,2,8,8)
