# Checkpoint+idempotency demonstration, no scheduler needed.
completed=set();written={}
def run(batch_id,rows,fail_once=False):
    if batch_id in completed:return 'SKIP'
    if fail_once: raise RuntimeError('transient failure')
    for r in rows:written[r['id']]=r
    completed.add(batch_id);return 'OK'
rows=[{'id':1,'x':2}]
try:run('batch-1',rows,True)
except RuntimeError:pass
assert run('batch-1',rows)=='OK'
assert run('batch-1',rows)=='SKIP' and len(written)==1
