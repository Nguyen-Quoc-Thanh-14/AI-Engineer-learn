from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
x,y=make_classification(n_samples=200,n_features=8,n_informative=4,random_state=3)
a,b,ya,yb=train_test_split(x,y,test_size=.25,random_state=42,stratify=y)
tree=DecisionTreeClassifier(random_state=1).fit(a,ya)
forest=RandomForestClassifier(n_estimators=30,random_state=1).fit(a,ya)
assert 0<=accuracy_score(yb,tree.predict(b))<=1
assert 0<=accuracy_score(yb,forest.predict(b))<=1
# Accuracy on one split does NOT prove lower estimator variance; repeat across splits/seeds for that claim.
