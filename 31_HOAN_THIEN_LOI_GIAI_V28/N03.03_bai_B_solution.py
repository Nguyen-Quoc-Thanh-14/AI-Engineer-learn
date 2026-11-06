import json,hashlib
# Toy append-only hash chain for audit events; NOT a replacement for externally anchored tamper-evident logging.
events=[];prev='0'*64
for kind in ('auth_success','data_export','logout'):
    event={'request_id':'req-7','event':kind,'prev_hash':prev}
    payload=json.dumps(event,sort_keys=True,separators=(',',':')).encode()
    prev=hashlib.sha256(payload).hexdigest();events.append((event,prev))
assert len(events)==3 and events[1][0]['prev_hash']==events[0][1]
# Persist to append-only storage with independent access control to resist malicious rewrite.
