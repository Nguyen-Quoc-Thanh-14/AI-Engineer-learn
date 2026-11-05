"""PT03.01 corrected: analytic gradient of f(x,y)=x^2+3xy vs finite difference."""
import math

def f(x:float,y:float)->float:
    return x*x + 3*x*y

def analytic_gradient(x:float,y:float)->tuple[float,float]:
    return 2*x + 3*y, 3*x

def finite_gradient(x:float,y:float,h:float=1e-5)->tuple[float,float]:
    if not math.isfinite(h) or h<=0:raise ValueError("positive finite step required")
    return ((f(x+h,y)-f(x-h,y))/(2*h),
            (f(x,y+h)-f(x,y-h))/(2*h))

def check():
    for x,y in [(0.,0.),(1.,2.),(-3.,4.),(100.,-2.)]:
        exact=analytic_gradient(x,y)
        approx=finite_gradient(x,y)
        assert all(math.isclose(a,b,rel_tol=1e-8,abs_tol=1e-7)
                   for a,b in zip(exact,approx)),(x,y,exact,approx)
    assert analytic_gradient(2.,3.)==(13.,6.)
    for h in (0,-1,float("nan")):
        try:finite_gradient(1.,2.,h)
        except ValueError:pass
        else:raise AssertionError("bad step")
if __name__=="__main__":
    check()
    print("PASS PT03.01 analytic vs finite gradient")
