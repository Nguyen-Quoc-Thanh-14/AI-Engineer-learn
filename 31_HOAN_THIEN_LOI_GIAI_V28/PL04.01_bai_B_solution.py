import torch
from tempfile import TemporaryDirectory
from pathlib import Path

def step(model,opt,x,y):
    opt.zero_grad();loss=((model(x)-y)**2).mean();loss.backward();opt.step()
x=torch.tensor([[1.],[2.]]);y=2*x
with TemporaryDirectory() as td:
    torch.manual_seed(7);m=torch.nn.Linear(1,1);opt=torch.optim.SGD(m.parameters(),lr=.01,momentum=.9)
    step(m,opt,x,y)
    p=Path(td)/'checkpoint.pt';torch.save({'model':m.state_dict(),'optimizer':opt.state_dict()},p)
    step(m,opt,x,y);continuous=[t.detach().clone() for t in m.parameters()]
    torch.manual_seed(99);r=torch.nn.Linear(1,1);opt2=torch.optim.SGD(r.parameters(),lr=.01,momentum=.9)
    ck=torch.load(p,map_location='cpu',weights_only=True);r.load_state_dict(ck['model']);opt2.load_state_dict(ck['optimizer'])
    step(r,opt2,x,y)
    assert all(torch.allclose(a,b) for a,b in zip(continuous,r.parameters()))
