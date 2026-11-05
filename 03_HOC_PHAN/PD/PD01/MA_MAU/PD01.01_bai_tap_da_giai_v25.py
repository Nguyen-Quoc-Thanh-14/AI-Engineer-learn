"""PD01.01 corrected: NumPy basic slice x[:, 1] is a view, not a copy."""
import numpy as np

def view_vs_copy():
    x=np.arange(12,dtype=np.int64).reshape(4,3)
    view=x[:,1]
    assert view.shape==(4,)
    assert np.shares_memory(view,x)
    old=int(x[0,1])
    view[0]=999
    assert x[0,1]==999 and old==1
    snapshot=x[:,1].copy()
    assert not np.shares_memory(snapshot,x)
    snapshot[0]=-42
    assert x[0,1]==999
    return x,view,snapshot

def check():
    x,view,snapshot=view_vs_copy()
    assert x.shape==(4,3)
    assert view.shape==(4,)
    assert snapshot[0]==-42 and view[0]==999
    empty=np.empty((0,3),dtype=int)
    assert empty[:,1].shape==(0,)
    try:
        np.ones((2,1))[:,1]
    except IndexError:pass
    else:raise AssertionError("missing second column")
if __name__=="__main__":
    check()
    print("PASS PD01.01 view aliasing shape")
