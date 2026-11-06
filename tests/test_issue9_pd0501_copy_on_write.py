"""PD05.01 pandas 3.x exact behavior and source-bound tests."""
from pathlib import Path
import runpy
import unittest
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"03_HOC_PHAN/PD/PD05/MA_MAU/PD05.01_bai_B_cow.py"
class PD0501Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=runpy.run_path(str(SRC))
    def test_actual_pandas_3_cow_and_loc_semantics(self):
        data=self.m["compare_edits"]()
        self.assertEqual(data["pandas_version"],pd.__version__)
        self.assertTrue(pd.__version__.startswith("3."))
        self.assertEqual(data["copy_value"],99)
        self.assertEqual(data["original_after_chained"],[1,2,3])
        self.assertEqual(data["original_after_loc"],[42,42,42])
    def test_negative_assignment_does_not_mutate_source(self):
        data=self.m["compare_edits"]()
        self.assertNotEqual(data["original_after_chained"],data["original_after_loc"])

if __name__=="__main__":
    unittest.main()
