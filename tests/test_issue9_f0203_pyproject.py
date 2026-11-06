"""F02.03: the B contract requires a real TOML file, not an in-memory string."""
from pathlib import Path
from tempfile import TemporaryDirectory
import ast
import runpy
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "03_HOC_PHAN/F/F02/MA_MAU/F02.03_bai_tap_da_giai_v27.py"
LESSON = ROOT / "03_HOC_PHAN/F/F02/BAI_HOC/F02.03.md"

class F0203ProjectFileTests(unittest.TestCase):
    def test_creates_actual_file_and_reads_optional_dependencies(self):
        writer = runpy.run_path(str(SCRIPT))["write_and_read_project"]
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "pyproject.toml"
            self.assertFalse(path.exists())
            parsed = writer(path)
            self.assertTrue(path.is_file())
            with path.open("rb") as stream:
                disk = tomllib.load(stream)
            self.assertEqual(parsed, disk)
            self.assertEqual(parsed["project"]["name"], "my-demo")
            self.assertIn("pytest>=8", parsed["project"]["optional-dependencies"]["dev"])

    def test_missing_directory_fails_instead_of_faking_success(self):
        writer = runpy.run_path(str(SCRIPT))["write_and_read_project"]
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing" / "pyproject.toml"
            with self.assertRaises(FileNotFoundError):
                writer(path)
            self.assertFalse(path.exists())

    def test_source_uses_disk_io_and_prompt_requires_real_file(self):
        code = SCRIPT.read_text(encoding="utf-8")
        tree = ast.parse(code)
        calls = [ast.unparse(n.func) for n in ast.walk(tree)
                 if isinstance(n, ast.Call)]
        self.assertIn("path.write_text", calls)
        self.assertIn("path.open", calls)
        self.assertIn("tomllib.load", calls)
        self.assertIn("Tạo file TOML với optional-dependencies", LESSON.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
