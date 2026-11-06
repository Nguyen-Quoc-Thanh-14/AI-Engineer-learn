# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from dataclasses import dataclass
@dataclass(frozen=True)
class Doc:
    id:str;tenant:str;content:str
def retrieve(query,tenant,docs):
    tokens=query.lower().split()
    allowed=[d for d in docs if d.tenant==tenant]
    return sorted(allowed,key=lambda d:sum(t in d.content.lower() for t in tokens),reverse=True)
docs=[Doc('a','A','python security'),Doc('b','B','python private data')]
assert [d.id for d in retrieve('python','A',docs)]==['a']
assert [d.id for d in retrieve('python','B',docs)]==['b']
assert retrieve('python','C',docs)==[]
# Lọc tenant TRƯỚC khi chọn và đưa tài liệu vào prompt, không chỉ sau khi LLM sinh.
print('PASS PN02.03')
