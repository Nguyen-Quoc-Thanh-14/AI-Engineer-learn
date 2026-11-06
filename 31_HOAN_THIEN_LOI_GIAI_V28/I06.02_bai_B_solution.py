def greedy(amount, coins=(1,3,4)):
    picked=[]
    for coin in sorted(coins,reverse=True):
        n,amount=divmod(amount,coin);picked.extend([coin]*n)
    return picked

def exact(amount, coins=(1,3,4)):
    if amount<0: raise ValueError('amount')
    best=[None]*(amount+1);best[0]=[]
    for target in range(1,amount+1):
        choices=[best[target-c]+[c] for c in coins if c<=target and best[target-c] is not None]
        best[target]=min(choices,key=len) if choices else None
    return best[amount]
assert len(greedy(6))==3 and len(exact(6))==2
assert exact(0)==[] and exact(7) is not None
