# coding: utf-8
# Bài J05.03 — Tài liệu có thể thực thi độc lập
class Service:
    def read(self): return 'ok'
commands={'read':Service().read}
assert commands['read']()=='ok'
assert 'delete_all' not in commands
