import torch
from torch import nn
torch.manual_seed(42)
m=nn.Sequential(nn.Linear(4,8),nn.Dropout(0.5),nn.Linear(8,1))
x=torch.ones(1,4)
m.eval()
with torch.inference_mode(): a=m(x);b=m(x)
assert torch.equal(a,b)
m.train();assert m[1].training is True
# Train mode changes dropout behavior, but individual outputs may coincidentally match.
