import torch
logits=torch.arange(16,dtype=torch.float32).reshape(4,4)
mask=torch.triu(torch.ones(4,4,dtype=torch.bool),diagonal=1)
att=torch.softmax(logits.masked_fill(mask,float('-inf')),dim=-1)
assert torch.allclose(att.sum(dim=-1),torch.ones(4))
assert torch.count_nonzero(att[0,1:])==0
