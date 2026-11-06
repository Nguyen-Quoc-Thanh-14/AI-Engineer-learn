# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
class Breaker:
    def __init__(self,clock,threshold=2,cooldown=5):
        self.clock=clock;self.threshold=threshold;self.cooldown=cooldown;self.fail=0;self.until=0
    def call(self,fn):
        if self.clock()<self.until:raise RuntimeError('OPEN')
        try: result=fn()
        except Exception:
            self.fail+=1
            if self.fail>=self.threshold:self.until=self.clock()+self.cooldown
            raise
        else:self.fail=0;self.until=0;return result
now=[0];b=Breaker(lambda:now[0])
def fail():raise TimeoutError
for _ in range(2):
    try:b.call(fail)
    except TimeoutError:pass
    else:raise AssertionError
try:b.call(lambda:'ok')
except RuntimeError:pass
else:raise AssertionError
now[0]=5;assert b.call(lambda:'ok')=='ok'
print('PASS N03.02')
