#!/usr/bin/env python3
"""Build-system regression tests, not academic course certification."""
import csv
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
spec=importlib.util.spec_from_file_location("publication_builder",HERE/"build.py")
builder=importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class PublicationTests(unittest.TestCase):
    def test_expected_441_unique_lessons_and_137_chapters(self):
        items,counts,chapters=builder.verify_source_inventory()
        self.assertEqual(len(items),441)
        self.assertEqual(len(chapters),137)
        self.assertEqual(len(counts),26)
        self.assertEqual(sum(counts.values()),441)

    def test_copy_source_preserves_code_and_removes_number_prefixes(self):
        origin=ROOT/"03_HOC_PHAN/A/A01/BAI_HOC/A01.01.md"
        original=origin.read_text(encoding="utf8")
        clean,count=builder.adapt_source(original,origin,"a"*40,[])
        self.assertGreater(count,0)
        self.assertIn("print(",clean)
        self.assertIn("A01.01 —",clean)
        self.assertIn("### A01.01 —",clean)
        self.assertNotIn("#### 11. ",clean)
        self.assertIn("https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/blob/"+"a"*40,clean)
        self.assertEqual(original,origin.read_text(encoding="utf8"))

    def test_inline_code_is_not_a_fake_markdown_link(self):
        origin=ROOT/"03_HOC_PHAN/D/D06/BAI_HOC/D06.01.md"
        tick=chr(96)
        warnings=[]
        src="Dùng "+tick+"def first[T](...)"+tick+" và [mã mẫu](../MA_MAU/D06.01_demo.py)"
        out=builder.rewrite_links(src,origin,"a"*40,warnings)
        self.assertIn(tick+"def first[T](...)"+tick,out)
        self.assertIn("/blob/"+"a"*40+"/03_HOC_PHAN/D/D06/MA_MAU/D06.01_demo.py",out)
        self.assertEqual(warnings,[])
        src2="Dùng "+tick+"def f[T](type_expr: TypeForm[T], value: T) -> T"+tick+"."
        self.assertEqual(builder.rewrite_links(src2,origin,"a"*40,warnings),src2)
        self.assertEqual(warnings,[])

    def test_produced_5_plus_5_manuscripts_and_sha_map(self):
        with tempfile.TemporaryDirectory(prefix="book_test_") as directory:
            destination=Path(directory)/"build"
            manifest,warnings=builder.build(output=destination,sha="b"*40)
            self.assertEqual(manifest["source_lessons"],441)
            self.assertEqual(manifest["source_chapters"],137)
            self.assertEqual(manifest["source_commit"],"b"*40)
            self.assertEqual(manifest["status"],"EDITORIAL_PREVIEW_NOT_RELEASED")
            self.assertEqual(len(manifest["volumes"]),5)
            self.assertEqual(sum(x["lesson_count"] for x in manifest["volumes"]),441)
            self.assertEqual(len(list(destination.glob("TAP_*_HOC_VIEN.md"))),5)
            self.assertEqual(len(list(destination.glob("TAP_*_LOI_GIAI.md"))),5)
            self.assertEqual(len(list(destination.glob("TAP_*.html"))),10)
            with (destination/"source_map.csv").open(encoding="utf8",newline="") as fp:
                records=list(csv.DictReader(fp))
            self.assertEqual(len(records),441)
            self.assertEqual(len({r["lesson_id"] for r in records}),441)
            self.assertEqual(len(manifest["generated_sha256"]),20)
            self.assertTrue((destination/"editorial_warnings.json").is_file())
            self.assertGreaterEqual(len(warnings),10)
            for volume in manifest["volumes"]:
                student=(destination/(volume["id"]+"_HOC_VIEN.md")).read_text(encoding="utf8")
                answer=(destination/(volume["id"]+"_LOI_GIAI.md")).read_text(encoding="utf8")
                self.assertIn("BẢN XEM TRƯỚC",student)
                self.assertIn("BẢN XEM TRƯỚC",answer)
                self.assertIn("## Lời nói đầu",student)
                self.assertIn("## Lời nói đầu",answer)
                self.assertEqual(len(re.findall(r'<a id="bai-[A-Z0-9-]+"></a>',student)),volume["lesson_count"])

if __name__=="__main__":
    unittest.main()
