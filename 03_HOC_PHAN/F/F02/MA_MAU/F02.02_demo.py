# coding: utf-8
# Bài F02.02 — Tài liệu có thể thực thi độc lập
from dataclasses import dataclass
@dataclass(frozen=True)
class Config: tax_rate: float

def total(price: float, cfg: Config) -> float:
    return round(price * (1 + cfg.tax_rate), 2)
assert total(100, Config(.1)) == 110.0
