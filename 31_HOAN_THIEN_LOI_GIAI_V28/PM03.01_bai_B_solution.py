import numpy as np
from sklearn.decomposition import PCA
x=np.array([[0.,1.],[1.,2.],[2.,2.],[3.,4.],[4.,4.]])
for k in (1,2):
    pca=PCA(n_components=k).fit(x)
    z=pca.transform(x);approx=pca.inverse_transform(z)
    error=np.mean((x-approx)**2)
    assert 0<=pca.explained_variance_ratio_.sum()<=1.000001
    if k==1:e1=error
    else:assert error<e1+1e-10
