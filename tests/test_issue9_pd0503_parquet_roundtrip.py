"""PD05.03 B must use a real PyArrow roundtrip with nulls and UTC timestamps."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import runpy
import unittest
import pyarrow as pa

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "03_HOC_PHAN/PD/PD05/MA_MAU/PD05.03_bai_B_parquet_roundtrip.py"

class PD0503ParquetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = runpy.run_path(str(SRC))
    def test_nullable_integer_timezone_schema_roundtrip(self):
        make = self.m["make_table"]
        t = make([None, 0, -8], [datetime(2026,1,d,tzinfo=timezone.utc) for d in (1,2,3)])
        self.assertEqual(t["qty"].null_count,1)
        self.assertEqual(t.schema.field("qty").type,pa.int64())
        self.assertTrue(t.schema.field("qty").nullable)
        self.assertEqual(t.schema.field("ts").type,pa.timestamp("us",tz="UTC"))
        with TemporaryDirectory() as d:
            got=self.m["roundtrip"](t,Path(d)/"test.parquet")
            self.assertTrue(got.equals(t))
    def test_timezone_aware_non_utc_normalizes_to_utc(self):
        local=timezone(timedelta(hours=7))
        t=self.m["make_table"]([1],[datetime(2026,1,2,7,tzinfo=local)])
        self.assertEqual(t.column("ts")[0].as_py(),datetime(2026,1,2,0,tzinfo=timezone.utc))
    def test_naive_timestamp_fails_closed(self):
        with self.assertRaises(ValueError):
            self.m["make_table"]([1],[datetime(2026,1,1)])
    def test_invalid_shapes_fail_closed(self):
        for quantities,times in (([],[]),([1],[]),([1,2],[datetime(2026,1,1,tzinfo=timezone.utc)])):
            with self.subTest(qty=quantities),self.assertRaises(ValueError):
                self.m["make_table"](quantities,times)

if __name__ == "__main__":
    unittest.main()
