def triangle(n):
    if n<0:raise ValueError('n')
    total=0
    for i in range(1,n+1):
        assert total==(i-1)*i//2  # loop invariant
        total+=i
    assert total==n*(n+1)//2
    return total
for n in range(100):assert triangle(n)==sum(range(n+1))
# Induction: base n=0; adding n+1 transforms n(n+1)/2 into (n+1)(n+2)/2.
