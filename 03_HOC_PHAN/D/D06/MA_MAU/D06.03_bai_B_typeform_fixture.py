"""D06.03 — executable CPython 3.15 TypedDict extra_items and TypeForm fixture."""
from typing import TypedDict, TypeForm

class Product(TypedDict, extra_items=int):
    name: str

def preserve_type_form[T](type_expr: TypeForm[T], value: T) -> T:
    """Type annotation demonstration ONLY; not runtime validation."""
    return value

item: Product = {"name": "notebook", "stock": 3}
assert Product.__extra_items__ is int
assert item["stock"] == 3
assert preserve_type_form(int, 3) == 3
print("D06.03_RUNTIME_TYPE_FORMS_PASS")
