# Debounce events with an injected monotonic clock, no external filesystem watcher needed.
def debounce(events,threshold=.2):
    by_path={}
    for when,path,kind in events:
        by_path[path]=(when,kind)
    return [(p,k) for p,(t,k) in sorted(by_path.items()) if events[-1][0]-t>=threshold]
changes=[(0.,'a.txt','modified'),(.05,'a.txt','modified'),(.5,'b.txt','renamed')]
assert debounce(changes)==[('a.txt','modified')]
# A real watchdog observer needs atomic move handling, path validation and queue backpressure.
