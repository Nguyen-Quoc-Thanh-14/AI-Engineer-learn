"""D06.03 runtime only: type checker compatibility is a separate explicit gate."""
import runpy
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TypeFormRuntime(unittest.TestCase):
    def test_exact_cpython_and_typed_extra_items(self):
        self.assertEqual(sys.version_info[:3],(3,15,2))
        p=ROOT/"03_HOC_PHAN/D/D06/MA_MAU/D06.03_bai_B_typeform_fixture.py"
        obj=runpy.run_path(str(p))
        self.assertIs(obj["Product"].__extra_items__,int)
        self.assertEqual(obj["item"]["stock"],3)
        self.assertEqual(obj["preserve_type_form"](int,3),3)

    def test_negative_fixture_is_not_an_accepted_script(self):
        p=ROOT/"03_HOC_PHAN/D/D06/MA_MAU/D06.03_bai_B_typeform_negative.py"
        source=p.read_text(encoding="utf8")
        self.assertIn('"many"',source)
        self.assertIn('extra_items=int',source)

if __name__=="__main__":
    unittest.main()
