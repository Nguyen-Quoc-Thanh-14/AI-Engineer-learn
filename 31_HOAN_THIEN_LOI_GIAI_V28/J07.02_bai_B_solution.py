import weakref,gc
class Node:
    def __init__(self): self.other=None
left=Node();right=Node();left.other=right;right.other=left
r=weakref.ref(left)
del left,right
gc.collect()
assert r() is None
# Explicit collect demonstrates cycle collection here; timing without it is not specified.
