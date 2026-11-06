"""Negative static type-checker fixture; do NOT execute as acceptance code."""
from typing import TypedDict
class Product(TypedDict, extra_items=int):
    name: str
bad: Product = {"name": "notebook", "stock": "many"}  # must be flagged
