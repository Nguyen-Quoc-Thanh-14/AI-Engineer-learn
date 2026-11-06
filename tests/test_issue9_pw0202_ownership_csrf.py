"""PW02.02 source-bound authorization and synthetic CSRF failure cases."""
from pathlib import Path
import runpy
import unittest

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"03_HOC_PHAN/PW/PW02/MA_MAU/PW02.02_bai_B_ownership_csrf.py"

class PW0202PolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=runpy.run_path(str(SRC))
        cls.session=cls.m["VerifiedSession"]("user-A","a"*32)
        cls.resource=cls.m["Record"]("user-A","original")
    def test_owner_and_session_token_must_both_match(self):
        result=self.m["update_record"](self.session,self.resource,"a"*32,"changed")
        self.assertEqual(result.text,"changed")
        self.assertEqual(self.resource.text,"original")
    def test_other_owner_denied(self):
        other=self.m["Record"]("user-B","secret")
        with self.assertRaises(self.m["NotAuthorized"]):
            self.m["update_record"](self.session,other,"a"*32,"steal")
        self.assertEqual(other.text,"secret")
    def test_missing_wrong_or_wrong_type_csrf_denied(self):
        for token in (None,"","b"*32,"a"*31,123):
            with self.subTest(token=token),self.assertRaises(self.m["InvalidCSRF"]):
                self.m["update_record"](self.session,self.resource,token,"changed")
    def test_untrusted_session_and_invalid_payload_denied(self):
        with self.assertRaises(self.m["NotAuthorized"]):
            self.m["update_record"]({"user_id":"user-A"},self.resource,"a"*32,"changed")
        with self.assertRaises(ValueError):
            self.m["update_record"](self.session,self.resource,"a"*32,"  ")
    def test_server_stored_csrf_token_does_not_log_secret(self):
        self.assertNotIn(self.session.csrf_secret,str(self.m["InvalidCSRF"]("invalid request token")))
        self.assertNotIn(self.session.csrf_secret,str(self.m["NotAuthorized"]("resource denied")))

if __name__ == "__main__":
    unittest.main()
