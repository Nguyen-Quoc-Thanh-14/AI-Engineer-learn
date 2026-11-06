# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from dataclasses import dataclass
@dataclass(frozen=True)
class User: id:int;role:str
@dataclass(frozen=True)
class Resource:owner_id:int

def can_read(user,resource):return user.role=='admin' or user.id==resource.owner_id
assert can_read(User(1,'user'),Resource(1))
assert not can_read(User(2,'user'),Resource(1))
assert can_read(User(2,'admin'),Resource(1))
# Vai trò không được suy ra từ trường do client tự gửi: cần xác thực server-side.
print('PASS N01.03')
