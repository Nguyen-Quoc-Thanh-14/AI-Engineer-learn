# coding: utf-8
# Bài N03.01 — Tài liệu có thể thực thi độc lập
def show_card(cache, backend):
    try: return backend()
    except TimeoutError: return cache
assert show_card('cached', lambda: (_ for _ in ()).throw(TimeoutError()))=='cached'
