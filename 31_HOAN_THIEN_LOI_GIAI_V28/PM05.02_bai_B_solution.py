# Threshold selected on validation data only, not test labels.
from sklearn.metrics import precision_score
probs=[.9,.8,.6,.2];truth=[1,1,0,0]
valid=[t for t in (.25,.5,.65,.75,.85) if precision_score(truth,[int(x>=t) for x in probs],zero_division=0)>=.95]
assert valid and min(valid)==.65
# For a real project, choose threshold using validation labels, then apply unchanged on test.
