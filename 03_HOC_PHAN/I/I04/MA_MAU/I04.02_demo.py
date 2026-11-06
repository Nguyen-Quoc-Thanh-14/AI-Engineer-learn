# coding: utf-8
# Bài I04.02 — Tài liệu có thể thực thi độc lập
tree = (2, (1,None,None), (3,None,None))
def inorder(t):
    if t is None: return []
    value, left, right = t
    return inorder(left) + [value] + inorder(right)
assert inorder(tree) == [1,2,3]
