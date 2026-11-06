import numpy as np
from tempfile import TemporaryDirectory
from pathlib import Path
x=np.arange(12,dtype=np.int64).reshape(3,4)
t=x.T
assert t.strides==(x.strides[1],x.strides[0]) and np.shares_memory(x,t)
y=t.copy();assert not np.shares_memory(x,y)
with TemporaryDirectory() as td:
    p=Path(td)/'matrix.npy';np.save(p,y)
    assert np.array_equal(np.load(p,allow_pickle=False),y)
