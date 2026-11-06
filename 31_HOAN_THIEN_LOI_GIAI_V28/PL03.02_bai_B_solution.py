# True means position blocked (cannot attend to future positions).
n=4;mask=[[j>i for j in range(n)] for i in range(n)]
assert mask==[[False,True,True,True],[False,False,True,True],[False,False,False,True],[False]*4]
for i in range(n):assert all(mask[i][j] for j in range(i+1,n))
