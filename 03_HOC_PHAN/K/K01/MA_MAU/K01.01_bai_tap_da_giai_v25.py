"""K01.01 corrected: timeit on n=1000 with median and observed spread."""
from statistics import median
from timeit import repeat

def squares_loop(n:int)->list[int]:
    values=[]
    for x in range(n):values.append(x*x)
    return values

def squares_comprehension(n:int)->list[int]:
    return [x*x for x in range(n)]

def measure(function,n:int=1000,repetitions:int=7,number:int=40)->dict:
    if type(n) is not int or n<0:raise ValueError("n nonnegative integer")
    if type(repetitions) is not int or repetitions<2:raise ValueError("repeat at least 2")
    if type(number) is not int or number<=0:raise ValueError("number positive")
    samples=repeat(lambda:function(n),repeat=repetitions,number=number)
    return {"n":n,"number":number,"samples":samples,"median_seconds":median(samples),
            "range_seconds":max(samples)-min(samples)}

def check():
    assert squares_loop(1000)==squares_comprehension(1000)
    for fn in (squares_loop,squares_comprehension):
        r=measure(fn)
        assert r["n"]==1000 and len(r["samples"])==7
        assert r["median_seconds"]>0 and r["range_seconds"]>=0
    try:measure(squares_loop,n=-1)
    except ValueError:pass
    else:raise AssertionError("negative input")
if __name__=="__main__":
    check()
    print("PASS K01.01",measure(squares_comprehension))
