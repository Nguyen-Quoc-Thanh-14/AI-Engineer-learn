# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from threading import Thread,Lock
balances=[1000,1000];common_lock=Lock()
def transfer(frm,to,amount):
    with common_lock:
        if amount<0 or balances[frm]<amount:raise ValueError
        balances[frm]-=amount;balances[to]+=amount
def worker():
    for _ in range(200): transfer(0,1,1);transfer(1,0,1)
ts=[Thread(target=worker) for _ in range(4)]
for t in ts:t.start()
for t in ts:t.join(timeout=3)
assert sum(balances)==2000
assert balances==[1000,1000]
print('PASS L06.02')
