import pandas as pd,numpy as np
from io import StringIO
csv='age,spend\n20,50\n30,100\n,70\n40,120\n'
df=pd.read_csv(StringIO(csv))
missing=df.isna().mean().mul(100).round(1).to_dict()
assert missing['age']==25.0 and len(df)==4
hist,edges=np.histogram(df['spend'],bins=3)
assert hist.sum()==4 and len(edges)==4
# EDA report should also inspect duplicates, outliers, group imbalance and data dictionary.
