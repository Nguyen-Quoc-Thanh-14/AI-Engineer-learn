# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from dataclasses import dataclass
@dataclass
class Node:
    value:int
    next:'Node|None'=None
def as_list(head):
    result=[];seen=set()
    while head is not None:
        if id(head) in seen: raise ValueError('cycle')
        seen.add(id(head));result.append(head.value);head=head.next
    return result
assert as_list(None)==[]
assert as_list(Node(1,Node(2)))==[1,2]
a=Node(1);a.next=a
try: as_list(a)
except ValueError: pass
else: raise AssertionError
print('PASS I03.02')
