def gradient_descent(x=0.,rate=.1,steps=60):
    history=[]
    for _ in range(steps):
        loss=(x-2)**2;history.append(loss)
        x-=rate*2*(x-2)
    return x,history
x,loss=gradient_descent()
assert abs(x-2)<1e-5 and loss[-1]<loss[0]
