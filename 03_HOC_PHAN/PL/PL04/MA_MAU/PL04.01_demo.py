# coding: utf-8
# Bài PL04.01 — Tài liệu có thể thực thi độc lập
import torch,io
m=torch.nn.Linear(2,1);buf=io.BytesIO();torch.save(m.state_dict(),buf)
buf.seek(0);state=torch.load(buf,weights_only=True)
assert 'weight' in state
