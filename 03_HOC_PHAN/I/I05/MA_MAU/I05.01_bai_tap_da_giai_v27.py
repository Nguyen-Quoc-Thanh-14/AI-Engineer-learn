# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def graph_from_edges(nodes,edges,directed=False):
    adj={n:set() for n in nodes}
    for u,v in edges:
        if u not in adj or v not in adj: raise ValueError('unknown node')
        adj[u].add(v)
        if not directed: adj[v].add(u)
    return adj
g=graph_from_edges(['a','b','c'],[('a','b')])
assert g['c']==set()
assert g['a']=={'b'} and g['b']=={'a'}
try: graph_from_edges(['a'],[('a','z')])
except ValueError: pass
else: raise AssertionError
print('PASS I05.01')
