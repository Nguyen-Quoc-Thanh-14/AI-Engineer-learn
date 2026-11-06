"""Source-bound behavior tests for three previously design-only B exercises."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import runpy
import unittest
import pyarrow as pa

ROOT=Path(__file__).resolve().parents[1]

class H06HypothesisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=runpy.run_path(str(ROOT/"03_HOC_PHAN/H/H06/MA_MAU/H06.01_bai_B_hypothesis.py"))

    def test_valid_sorted_property(self):
        self.m["test_builtin_sorted_keeps_length"]()

    def test_broken_sort_shrinks_to_one_element(self):
        example=self.m["shrink_counterexample"]()
        self.assertEqual(len(example),1)
        self.assertEqual(self.m["broken_sort"](example),[])
        self.assertEqual(self.m["broken_sort"]([]),[])

class PE02ParquetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=runpy.run_path(str(ROOT/"03_HOC_PHAN/PE/PE02/MA_MAU/PE02.01_bai_B_parquet.py"))

    def test_nullable_schema_and_data_roundtrip(self):
        t=self.m["create_table"](30)
        self.assertEqual(t.num_rows,30)
        self.assertGreater(t["value"].null_count,0)
        self.assertTrue(t.schema.equals(self.m["SCHEMA"]))
        self.assertTrue(t.schema.field("value").nullable)
        self.assertFalse(t.schema.field("sensor_id").nullable)
        self.assertEqual(t.schema.field("timestamp").type,pa.timestamp("us",tz="UTC"))
        with TemporaryDirectory() as d:
            sizes=self.m["roundtrip"](t,Path(d))
            self.assertGreater(sizes["snappy"],0)
            self.assertGreater(sizes["NONE"],0)

    def test_invalid_sample_count(self):
        for n in (0,-1,True,"5",None):
            with self.subTest(n=n),self.assertRaises(ValueError):
                self.m["create_table"](n)

class PS02SensorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=runpy.run_path(str(ROOT/"03_HOC_PHAN/PS/PS02/MA_MAU/PS02.03_bai_B_sensor_parquet.py"))

    def test_dst_timezones_are_two_distinct_instants(self):
        rows=self.m["validate_rows"](self.m["example_rows"]())
        self.assertLess(rows[0]["timestamp"],rows[1]["timestamp"])
        self.assertEqual(rows[0]["timestamp"].tzinfo,timezone.utc)
        self.assertEqual(rows[1]["timestamp"].tzinfo,timezone.utc)

    def test_nullable_dictionary_schema_and_hash(self):
        with TemporaryDirectory() as d:
            result=self.m["write_and_check"](self.m["example_rows"](),Path(d)/"reading.parquet")
            self.assertEqual(result["count"],2)
            self.assertEqual(result["nulls"],1)
            self.assertEqual(len(result["sha256"]),64)
            self.assertEqual(result["timezone"],"timestamp[us, tz=UTC]")

    def test_duplicate_timestamp_rejected(self):
        rows=self.m["example_rows"]()
        duplicate=dict(rows[1],timestamp=rows[0]["timestamp"])
        with self.assertRaises(ValueError):
            self.m["validate_rows"]([rows[0],duplicate])

    def test_mixed_units_rejected(self):
        rows=self.m["example_rows"]()
        invalid=dict(rows[1],unit="F")
        with self.assertRaises(ValueError):
            self.m["validate_rows"]([rows[0],invalid])

    def test_naive_datetime_rejected(self):
        rows=self.m["example_rows"]()
        bad=dict(rows[0],timestamp=datetime(2026,11,1,1,30))
        with self.assertRaises(ValueError):
            self.m["validate_rows"]([bad])

    def test_null_quality_mismatch_rejected(self):
        rows=self.m["example_rows"]()
        bad=dict(rows[1],quality_flag="ok")
        with self.assertRaises(ValueError):
            self.m["validate_rows"]([rows[0],bad])

    def test_invalid_inputs_rejected(self):
        f=self.m["validate_rows"]
        for rows in ([],None,["not a record"]):
            with self.subTest(rows=rows),self.assertRaises((TypeError,ValueError)):
                f(rows)

if __name__=="__main__":
    unittest.main()
