import random
# Clock injected: no sleeping or relying on wall clock for scheduler test.
class Job:
    def __init__(self,job_id): self.job_id=job_id;self.attempts=0
    def run(self,send):
        for delay in (0,1,2):
            self.attempts+=1
            try:return send(self.job_id)
            except ConnectionError:
                if delay==2:raise
        raise AssertionError('unreachable')
job=Job('job-003')
def fake_send(job_id):
    if job.attempts<3:raise ConnectionError('transient')
    return 'delivered:'+job_id
assert job.run(fake_send)=='delivered:job-003' and job.attempts==3
