# coding: utf-8
# Bài PA04.01 — Tài liệu có thể thực thi độc lập
def ensure_tag(tags,name):
    if name not in tags:tags.append(name)
    return tags
a=[];ensure_tag(a,'ok');ensure_tag(a,'ok')
assert a==['ok']
