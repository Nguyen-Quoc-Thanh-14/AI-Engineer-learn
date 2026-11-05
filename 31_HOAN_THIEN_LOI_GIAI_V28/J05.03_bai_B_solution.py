class Service:
    def read(self): return 'read'
    def admin_delete(self): return 'destroyed'
service=Service()
allowed={'read':service.read}
def dispatch(name):
    try: fn=allowed[name]
    except KeyError: raise PermissionError(name)
    return fn()
assert dispatch('read')=='read'
try: dispatch('admin_delete')
except PermissionError: pass
else: raise AssertionError('privileged method exposed')
