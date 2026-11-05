import torch
# Gradient of mean loss over four equal microbatches approximates one full batch update.
torch.manual_seed(0);x=torch.arange(8,dtype=torch.float32).reshape(-1,1)/10;y=2*x+1
full=torch.nn.Linear(1,1);micro=torch.nn.Linear(1,1);micro.load_state_dict(full.state_dict())
opt1=torch.optim.SGD(full.parameters(),lr=.1);opt2=torch.optim.SGD(micro.parameters(),lr=.1)
opt1.zero_grad();torch.nn.functional.mse_loss(full(x),y).backward();opt1.step()
opt2.zero_grad()
for xx,yy in zip(x.chunk(4),y.chunk(4)):(torch.nn.functional.mse_loss(micro(xx),yy)/4).backward()
opt2.step()
for p,q in zip(full.parameters(),micro.parameters()):assert torch.allclose(p,q,atol=1e-6)
