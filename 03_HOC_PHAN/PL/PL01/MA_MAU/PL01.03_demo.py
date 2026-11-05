# coding: utf-8
# Bài PL01.03 — Tài liệu có thể thực thi độc lập
import torch
device='cuda' if torch.cuda.is_available() else 'cpu'
x=torch.ones(2,device=device)
assert x.sum().item()==2
