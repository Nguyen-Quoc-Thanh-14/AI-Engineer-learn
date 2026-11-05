# coding: utf-8
# Bài J04.02 — Tài liệu có thể thực thi độc lập
class Registry:
    registry=[]
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Registry.registry.append(cls.__name__)
class Plugin(Registry): pass
assert 'Plugin' in Registry.registry
