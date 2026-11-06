"""Source-bound regression oracle for F05.02; no mocked lazy-import claims."""
import importlib.util
from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "03_HOC_PHAN/F/F05/MA_MAU/F05.02_bai_B_import_order.py"

@unittest.skipUnless(sys.implementation.name == "cpython" and sys.version_info[:2] == (3, 15),
                     "Requires CPython 3.15 explicit lazy imports")
class LazyImportOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("f0502_probe", SOURCE)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.probe = staticmethod(module.run_probe)

    def test_eager_module_initialized_before_main(self):
        a = self.probe("eager")
        self.assertEqual(a["exit_code"], 0, a["stderr"])
        self.assertEqual(a["stdout_lines"], ["MODULE_INITIALIZED", "MAIN_BEFORE", "VALUE 7"])

    def test_lazy_module_initialized_only_on_first_use(self):
        a = self.probe("lazy_used")
        self.assertEqual(a["exit_code"], 0, a["stderr"])
        self.assertEqual(a["stdout_lines"], ["MAIN_BEFORE", "MODULE_INITIALIZED", "VALUE 7"])

    def test_lazy_unused_module_never_initialized(self):
        a = self.probe("lazy_unused")
        self.assertEqual(a["exit_code"], 0, a["stderr"])
        self.assertEqual(a["stdout_lines"], ["MAIN_BEFORE", "MAIN_AFTER"])

    def test_lazy_import_error_is_deferred(self):
        a = self.probe("lazy_used", fail_on_import=True)
        self.assertNotEqual(a["exit_code"], 0)
        self.assertEqual(a["stdout_lines"], ["MAIN_BEFORE", "MODULE_INITIALIZED"])
        self.assertIn("synthetic import failure", a["stderr"])

    def test_eager_import_error_occurs_before_main(self):
        a = self.probe("eager", fail_on_import=True)
        self.assertNotEqual(a["exit_code"], 0)
        self.assertEqual(a["stdout_lines"], ["MODULE_INITIALIZED"])
        self.assertIn("synthetic import failure", a["stderr"])

    def test_invalid_mode_fails_closed(self):
        with self.assertRaises(ValueError):
            self.probe("bogus")

if __name__ == "__main__":
    unittest.main()
