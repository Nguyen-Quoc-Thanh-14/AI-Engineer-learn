import torch
from torch import nn
torch.manual_seed(7)
x=torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y=torch.tensor([[0.],[1.],[1.],[0.]])
linear=nn.Linear(2,1);mlp=nn.Sequential(nn.Linear(2,16),nn.Tanh(),nn.Linear(16,1))
opt=torch.optim.Adam(mlp.parameters(),lr=.08)
for _ in range(180):
    opt.zero_grad();loss=((mlp(x)-y)**2).mean();loss.backward();opt.step()
with torch.no_grad():
    preds=(mlp(x)>0.5).float()
    assert torch.equal(preds,y)
# A linear classifier cannot represent XOR with a single linear decision boundary.
