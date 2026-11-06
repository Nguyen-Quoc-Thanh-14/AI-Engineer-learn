import torch
p=torch.nn.Parameter(torch.tensor([0.]))
opt=torch.optim.SGD([p],lr=.1)
losses=[]
for _ in range(50):
    opt.zero_grad();loss=(p-3).square().sum();loss.backward();opt.step()
    losses.append(loss.item())
assert losses[-1]<losses[0]*1e-8
