# coding: utf-8
# Bài F05.02 — Tài liệu có thể thực thi độc lập
# Mã minh họa yêu cầu CPython 3.15+, không chạy trong môi trường 3.13:
lazy import decimal
assert decimal.Decimal('0.1') + decimal.Decimal('0.2') == decimal.Decimal('0.3')
