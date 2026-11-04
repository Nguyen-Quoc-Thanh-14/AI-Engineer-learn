# coding: utf-8
# Bài E03.03 — Tài liệu có thể thực thi độc lập
class Invoice:
    def __init__(self, items): self.items = items
    def total(self): return sum(price for price in self.items)
invoice = Invoice([100, 25])
assert invoice.total() == 125
assert not hasattr(invoice, 'totall')
