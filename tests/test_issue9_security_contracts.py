"""Issue #9 source-bound security checks. Automated checks are not expert review."""
import runpy
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class SecurityLessonContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n02=runpy.run_path(str(ROOT/"31_HOAN_THIEN_LOI_GIAI_V28/N02.01_bai_B_solution.py"))
        cls.f04=runpy.run_path(str(ROOT/"31_HOAN_THIEN_LOI_GIAI_V28/F04.01_bai_B_solution.py"))

    def test_n02_redacts_sensitive_fields(self):
        s=self.n02["demo_log"]('token=NEVER_LOG_FAKE api_key="OTHER_FAKE"')
        self.assertEqual(s.count("[REDACTED]"),2)
        self.assertNotIn("NEVER_LOG_FAKE",s)
        self.assertNotIn("OTHER_FAKE",s)

    def test_n02_non_sensitive_message_unchanged(self):
        self.assertEqual(self.n02["demo_log"]("status=ok").strip(),"status=ok")

    def test_n02_non_string_rejected(self):
        for val in (None,17,False,b"token=demo"):
            with self.subTest(val=val),self.assertRaises(TypeError):
                self.n02["demo_log"](val)

    def test_n02_has_genuine_rotation_checklist(self):
        s=(ROOT/"03_HOC_PHAN/N/N02/LOI_GIAI/N02.01_loi_giai.md").read_text(encoding="utf8").casefold()
        for term in ("cô lập","vô hiệu hóa","phát hành key mới","phụ thuộc","giám sát","quét history"):
            self.assertIn(term,s)
        self.assertIn("không tự xoay vòng một key thật",s)

    def test_f04_request_id_and_real_redaction(self):
        s=self.f04["render_log"]("done token=FAKE_TEST_KEY","req-42")
        self.assertTrue(s.startswith("req-42 "),s)
        self.assertIn("token=[REDACTED]",s)
        self.assertNotIn("FAKE_TEST_KEY",s)

    def test_f04_invalid_id_cannot_inject_log(self):
        for invalid in ("bad\nid","bad\rid","x"*65,"", " key=value","đề-nghị"):
            with self.subTest(invalid=invalid):
                s=self.f04["render_log"]("status=ok",invalid)
                self.assertTrue(s.startswith("invalid-id "),s)
                if invalid: self.assertNotIn(invalid,s)

    def test_f04_context_reset_after_request(self):
        self.f04["render_log"]("status=ok","req-111")
        self.assertEqual(self.f04["request_id"].get(),"-")
        s=self.f04["render_log"]("status=ok","req-222")
        self.assertTrue(s.startswith("req-222 "))
        self.assertNotIn("req-111",s)

    def test_f04_arg_type_rejected(self):
        for args in ((None,"req-1"),("ok",3)):
            with self.subTest(args=args),self.assertRaises(TypeError):
                self.f04["render_log"](*args)

    def test_f04_quoted_token_and_key(self):
        s=self.f04["render_log"]("""token="FAKE_ONE" api_key='FAKE_TWO'""","req-42")
        self.assertEqual(s.count("[REDACTED]"),2)
        self.assertNotIn("FAKE_ONE",s)
        self.assertNotIn("FAKE_TWO",s)

    def test_n02_and_f04_B_requirements_preserved(self):
        for name,part,chapter,fragment in (
            ("N02.01","N","N02","checklist rotate API key khi bị lộ"),
            ("F04.01","F","F04","context request ID vào LogRecord"),
        ):
            path=ROOT/f"03_HOC_PHAN/{part}/{chapter}/BAI_HOC/{name}.md"
            self.assertIn(fragment,path.read_text(encoding="utf8"))

if __name__=="__main__":
    unittest.main()
