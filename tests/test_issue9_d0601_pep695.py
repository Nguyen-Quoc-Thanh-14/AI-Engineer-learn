"""D06.01: source-bound PEP 695 syntax and runtime contract, not academic review."""
import ast
from pathlib import Path
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "03_HOC_PHAN/D/D06/MA_MAU/D06.01_bai_tap_da_giai_v27.py"
LESSON = ROOT / "03_HOC_PHAN/D/D06/BAI_HOC/D06.01.md"

class D0601Pep695Tests(unittest.TestCase):
    def test_implements_literal_generic_first_type_parameter(self):
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        first = next(n for n in tree.body
                     if isinstance(n, ast.FunctionDef) and n.name == "first")
        self.assertEqual(len(first.type_params), 1)
        self.assertIsInstance(first.type_params[0], ast.TypeVar)
        self.assertEqual(first.type_params[0].name, "T")
        self.assertEqual(ast.unparse(first.args.args[0].annotation), "list[T]")
        self.assertEqual(ast.unparse(first.returns), "T")

    def test_function_works_for_multiple_types_and_rejects_empty(self):
        first = runpy.run_path(str(SCRIPT))["first"]
        self.assertEqual(first([7, 9]), 7)
        self.assertEqual(first(["a", "b"]), "a")
        self.assertEqual(first([(1, 2)]), (1, 2))
        with self.assertRaises(ValueError):
            first([])

    def test_b_prompt_actually_requires_pep695_syntax(self):
        lesson = LESSON.read_text(encoding="utf-8")
        self.assertIn("Tạo generic `first[T](items:list[T])->T`", lesson)

if __name__ == "__main__":
    unittest.main()
