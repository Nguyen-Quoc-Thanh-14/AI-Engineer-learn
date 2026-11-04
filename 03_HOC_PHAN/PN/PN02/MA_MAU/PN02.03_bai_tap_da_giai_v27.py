# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
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
