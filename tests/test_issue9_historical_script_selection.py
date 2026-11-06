"""Guard against silently ignoring historical v25 exercise scripts."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"tests"))
import issue9_v27_b_runtime_3152 as mod

V25_IDS = ("A01.01", "B09.01", "C03.01", "D02.01", "E03.01", "G01.01",
           "J02.01", "L02.01", "PA04.01", "PE03.01", "PL01.01", "PM01.02")

class HistoricalBSelection(unittest.TestCase):
    def test_v25_twelve_are_real_files_not_missing(self):
        for lesson in V25_IDS:
            part = lesson.rstrip("0123456789.").strip()
            chapter = lesson.split(".")[0]
            with self.subTest(id=lesson):
                path, ver = mod.select_script(ROOT/"03_HOC_PHAN"/part/chapter, lesson)
                self.assertEqual(ver, "v25")
                self.assertTrue(path.is_file())
                self.assertIn("def check()", path.read_text(encoding="utf-8"))
                self.assertIn("OK " + lesson, path.read_text(encoding="utf-8"))

    def test_v27_has_precedence(self):
        path, ver = mod.select_script(ROOT/"03_HOC_PHAN"/"D"/"D06", "D06.02")
        self.assertEqual(ver, "v27")
        self.assertTrue(path.is_file())

    def test_nonexistent_script_fails_to_resolve(self):
        path, ver = mod.select_script(ROOT/"03_HOC_PHAN"/"A"/"A01", "A01.99")
        self.assertIsNone(path)
        self.assertIsNone(ver)

if __name__ == "__main__":
    unittest.main()
