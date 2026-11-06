"""Synthetic mini-repos validate Issue 9 triage and fail-closed behavior."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
import issue9_content_inventory as audit

class TriageUnitTests(unittest.TestCase):
    def seed(self,root,id_,prompt,answer_prompt=None):
        letters="".join(ch for ch in id_ if ch.isalpha())
        chapter=id_.split(".")[0]
        folder=root/"03_HOC_PHAN"/letters/chapter
        lesson=folder/"BAI_HOC"/(id_+".md")
        answer=folder/"LOI_GIAI"/(id_+"_loi_giai.md")
        demo=folder/"MA_MAU"/(id_+"_demo.py")
        b=root/"31_HOAN_THIEN_LOI_GIAI_V28"/(id_+"_bai_B_solution.py")
        for p in (lesson,answer,demo,b):p.parent.mkdir(parents=True,exist_ok=True)
        lesson.write_text(f"# {id_}\n**Bài B — Ứng dụng:** {prompt}\n",encoding="utf8")
        answer.write_text(
            f"# {id_}\n**Đề bài:** {answer_prompt or prompt}\n"+
            "\n"+chr(96)*3+"python\nassert True\n"+chr(96)*3+"\n",encoding="utf8")
        demo.write_text("print('ok')\n",encoding="utf8")
        b.write_text("assert True\n",encoding="utf8")
        return lesson,answer,demo,b

    def test_detects_mismatch_candidate_not_certification(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.seed(root,"F04.01","log user request with request ID")
            self.seed(root,"N02.01","rotate exposed key and hide secrets","train a neural network")
            rows,errors=audit.audit(root,expected_lessons=2,expected_programs=2)
            self.assertFalse(errors)
            self.assertEqual(len(rows),2)
            flagged=[r for r in rows if "B_VS_ANSWER_PROMPT_CANDIDATE" in r["candidate_flags"]]
            self.assertEqual([r["lesson_id"] for r in flagged],["N02.01"])

    def test_missing_demo_is_blocking(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            *_,b=self.seed(root,"F04.01","test requests")
            (root/"03_HOC_PHAN/F/F04/MA_MAU/F04.01_demo.py").unlink()
            _,errors=audit.audit(root,expected_lessons=1,expected_programs=1)
            self.assertTrue(any("MISSING_DEMO" in s for s in errors))

    def test_invalid_B_syntax_is_blocking(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            *_,b=self.seed(root,"F04.01","test requests")
            b.write_text("def f(\n",encoding="utf8")
            rows,errors=audit.audit(root,expected_lessons=1,expected_programs=1)
            self.assertIn("B_SCRIPT_SYNTAX_ERROR",rows[0]["candidate_flags"])
            self.assertTrue(errors)

    def test_missing_program_count_is_blocking(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            *_,b=self.seed(root,"N02.01","rotate key")
            b.unlink()
            _,errors=audit.audit(root,expected_lessons=1,expected_programs=1)
            self.assertTrue(any("B_PROGRAM_COUNT" in e for e in errors))

    def test_staleness_is_only_a_signal(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            lesson,*_=self.seed(root,"N02.01","rotate key")
            lesson.write_text(lesson.read_text()+"Chưa kiểm định trực tiếp trên CPython 3.15.2.\n")
            rows,errors=audit.audit(root,expected_lessons=1,expected_programs=1)
            self.assertFalse(errors)
            self.assertIn("POSSIBLE_STALE_VERSION_CLAIM",rows[0]["candidate_flags"])

if __name__=="__main__":
    unittest.main()
