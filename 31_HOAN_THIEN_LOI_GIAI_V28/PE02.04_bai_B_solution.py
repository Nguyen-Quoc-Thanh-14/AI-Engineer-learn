def should_alert(previous_rows,new_rows,freshness_seconds):
    if previous_rows<0 or new_rows<0:raise ValueError('row count')
    row_drop=(previous_rows>0 and new_rows<.4*previous_rows)
    stale=freshness_seconds>7200
    return {'row_drop':row_drop,'stale':stale,'alert':row_drop or stale}
assert should_alert(100,39,1)['row_drop']
assert not should_alert(100,40,7200)['alert']
assert should_alert(100,100,7201)['stale']
