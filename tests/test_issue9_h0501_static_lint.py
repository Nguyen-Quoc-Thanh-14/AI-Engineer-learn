"""Source-bound H05.01 checker negative oracle."""
from pathlib import Path
import ast
import runpy
import unittest
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"03_HOC_PHAN/H/H05/MA_MAU/H05.01_bai_B_static_lint.py"
class H0501Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=runpy.run_path(str(SRC))
    def test_real_ruff_pyright_reject_bad_and_accept_good(self):
        observed=self.m["check_quality_gates"]()
        self.assertEqual(observed["status"],"QUALITY_GATES_PASS")
        self.assertTrue(observed["ruff_version"])
        self.assertTrue(observed["pyright_version"])
        for name,expected in [("ruff_good",0),("pyright_good",0)]:
            self.assertEqual(observed["results"][name]["exit"],expected)
        for name in ("ruff_bad","pyright_bad"):
            self.assertNotEqual(observed["results"][name]["exit"],0)
    def test_negative_source_includes_static_type_error_and_ruff_violation(self):
        self.assertIn('count: int = "bad type"',self.m["BAD"])
        self.assertIn("import os",self.m["BAD"])
        ast.parse(self.m["GOOD"])
        ast.parse(self.m["BAD"])

if __name__ == "__main__":
    unittest.main()
