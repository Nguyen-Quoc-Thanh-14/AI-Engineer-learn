# coding: utf-8
# Bài J07.01 — Tài liệu có thể thực thi độc lập
from types import MappingProxyType
source={'a':1}
view=MappingProxyType(source)
assert view['a']==1
source['a']=2
assert view['a']==2
