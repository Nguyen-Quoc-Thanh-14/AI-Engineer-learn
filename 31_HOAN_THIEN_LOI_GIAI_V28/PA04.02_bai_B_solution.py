# Alert after three consecutive failed runs, reset on success.
class Heartbeat:
    def __init__(self):self.failures=0;self.alerts=[]
    def record(self,success):
        self.failures=0 if success else self.failures+1
        if self.failures==3:self.alerts.append('ALERT')
h=Heartbeat()
for ok in (False,False,True,False,False,False,False):h.record(ok)
assert h.alerts==['ALERT'] and h.failures==4
