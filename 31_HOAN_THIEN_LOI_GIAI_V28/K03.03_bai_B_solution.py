from io import StringIO
class Batcher:
    def __init__(self,max_count=3):
        if max_count<=0:raise ValueError('max_count')
        self.max_count=max_count;self.pending=[];self.sink=StringIO()
    def add(self,x):
        self.pending.append(str(x))
        if len(self.pending)>=self.max_count:self.flush()
    def flush(self):
        if self.pending:self.sink.write(','.join(self.pending)+'\n');self.pending.clear()
b=Batcher(3)
for n in range(10):b.add(n);assert len(b.pending)<=2
b.flush()
assert b.sink.getvalue().splitlines()==['0,1,2','3,4,5','6,7,8','9']
# Max-delay requires an actual timer/clock parameter; max-count alone cannot guarantee latency.
