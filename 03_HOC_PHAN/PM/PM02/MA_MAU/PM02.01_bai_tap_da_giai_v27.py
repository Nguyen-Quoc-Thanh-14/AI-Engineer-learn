# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso,Ridge
X,y=make_regression(n_samples=100,n_features=3,noise=2,random_state=4)
train,test=train_test_split(range(len(y)),test_size=.25,random_state=2)
metrics=[]
for model in (Lasso(alpha=1),Ridge(alpha=1)):
    model.fit(X[train],y[train])
    metrics.append((model.intercept_,model.coef_.copy(),model.score(X[test],y[test])))
assert all(len(coef)==3 for _,coef,_ in metrics)
assert all(isinstance(float(intercept),float) for intercept,_,_ in metrics)
assert len(metrics)==2
print('PASS PM02.01')
