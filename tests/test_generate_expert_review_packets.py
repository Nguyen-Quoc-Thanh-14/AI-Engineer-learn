"""Synthetic fixtures verifying coverage and fail-closed packet generation."""
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
from generate_expert_review_packets import build

class ReviewPacketTests(unittest.TestCase):
    def fixture(self,root,code,part):
        base=root/"03_HOC_PHAN"/part/code.split(".")[0]
        files=[base/"BAI_HOC"/(code+".md"),
               base/"LOI_GIAI"/(code+"_loi_giai.md"),
               base/"MA_MAU"/(code+"_demo.py")]
        for f in files:
            f.parent.mkdir(parents=True,exist_ok=True)
            f.write_text(f.name,encoding="utf8")
        return files

    def test_exact_slots_source_sha_and_no_forged_review(self):
        with TemporaryDirectory() as d:
            root=Path(d)
            self.fixture(root,"A01.01","A")
            changed=self.fixture(root,"N01.01","N")[0]
            rows=build(root,expected=2)
            self.assertEqual([x["assignment_id"] for x in rows],
                             ["A01.01-R1","N01.01-R1","N01.01-R2"])
            self.assertEqual(rows,build(root,expected=2))
            self.assertTrue(all(x["reviewer_github"]=="" and
                                x["state"]=="AWAITING_EXTERNAL_HUMAN"
                                for x in rows))
            old=rows[1]["lesson_sha256"]
            changed.write_text("new source",encoding="utf8")
            self.assertNotEqual(old,build(root,expected=2)[1]["lesson_sha256"])

    def test_missing_file_is_not_silently_omitted(self):
        with TemporaryDirectory() as d:
            root=Path(d)
            files=self.fixture(root,"L01.01","L")
            files[1].unlink()
            with self.assertRaises(ValueError):
                build(root,expected=1)

    def test_duplicate_lesson_id_rejected(self):
        with TemporaryDirectory() as d:
            root=Path(d)
            self.fixture(root,"A01.01","A")
            self.fixture(root,"A01.01","X")
            with self.assertRaises(ValueError):
                build(root,expected=2)

if __name__=="__main__":
    unittest.main()
