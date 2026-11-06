"""F01.01 corrected: import statistics and calculate mean of nonempty numbers."""
import math
import statistics

def nonempty_mean(values: list[int | float]) -> float:
    if not isinstance(values,list):
        raise TypeError("values must be a list")
    if not values:
        raise ValueError("mean of empty list is undefined")
    if any(type(v) not in (int,float) or not (0<=v or v<0) or
           (type(v) is float and not math.isfinite(v)) for v in values):
        raise ValueError("only finite int/float values allowed, excluding bool")
    return float(statistics.mean(values))

def check():
    assert nonempty_mean([1,2,3])==2.0
    assert nonempty_mean([-4,4])==0.0
    assert nonempty_mean([5])==5.0
    assert nonempty_mean([0,0,0])==0.0
    for bad in ([], [float("nan")], [float("inf")], [True,1], ["3",5]):
        try:nonempty_mean(bad)
        except ValueError:pass
        else:raise AssertionError(repr(bad))
    try:nonempty_mean((1,2))
    except TypeError:pass
    else:raise AssertionError("not a list")
if __name__=="__main__":
    check()
    print("PASS F01.01 mean")
