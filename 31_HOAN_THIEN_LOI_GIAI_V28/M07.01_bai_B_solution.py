# Expand-and-contract: release 1 read old + new; release 2 write both; release 3 stop old.
def rename_compat(record):
    if 'display_name' in record:return record['display_name']
    if 'name' in record:return record['name']
    raise ValueError('missing display name')
assert rename_compat({'name':'old'})=='old'
assert rename_compat({'display_name':'new','name':'old'})=='new'
try:rename_compat({})
except ValueError:pass
else:raise AssertionError('missing field accepted')
