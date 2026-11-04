import statistics,time,sys
from dataclasses import dataclass
@dataclass(frozen=True)
class Report:
    p50_ms:float;p95_ms:float;peak_bytes:int;regression_tests_pass:bool;readability_notes:str
samples=[2,3,3,4,5,6,6,7,8,9]
report=Report(statistics.median(samples),sorted(samples)[int(.95*(len(samples)-1))],1024,True,'explicit loop is easier to debug')
assert report.p50_ms==5.5 and report.p95_ms==8
# p95 estimator must be named; this example uses nearest-rank index floor(0.95*(n-1)).
