# At-least-once deliveries: deduplicate with persistent idempotency key in production.
seen=set();applied=[]
def consume(message):
    key=message['event_id']
    if key in seen:return False
    seen.add(key);applied.append(message['value']);return True
assert consume({'event_id':'e1','value':4})
assert not consume({'event_id':'e1','value':4})
assert applied==[4]
