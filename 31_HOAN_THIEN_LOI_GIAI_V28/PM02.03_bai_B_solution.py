import numpy as np
from sklearn.calibration import calibration_curve
prob=np.array([.1,.2,.3,.7,.8,.9]);y=np.array([0,0,1,0,1,1])
truth,confidence=calibration_curve(y,prob,n_bins=3,strategy='uniform')
assert len(truth)==len(confidence) and np.all((0<=confidence)&(confidence<=1))
# Reliability diagram requires plotting truth against confidence and adequate bin support.
