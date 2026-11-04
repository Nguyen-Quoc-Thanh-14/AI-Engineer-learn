# coding: utf-8
# Bài D06.03 — Tài liệu có thể thực thi độc lập
from typing import TypedDict
class User(TypedDict): name: str
u:User={'name':'An'}
assert u['name']=='An'
