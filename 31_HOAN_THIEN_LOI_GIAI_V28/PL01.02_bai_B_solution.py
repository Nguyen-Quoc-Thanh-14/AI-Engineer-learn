import math

def analytic(x): return math.sin(x)+x*math.cos(x)
def numeric(x,eps=1e-6):return ((x+eps)*math.sin(x+eps)-(x-eps)*math.sin(x-eps))/(2*eps)
for x in (-3.,-0.1,0.,2.):assert abs(analytic(x)-numeric(x))<1e-8
