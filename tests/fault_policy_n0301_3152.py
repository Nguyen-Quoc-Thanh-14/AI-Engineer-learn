"""Independent oracle for N03.01 dependency outage policy on CPython 3.15.2."""
from pathlib import Path
import hashlib
import json
import runpy
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "03_HOC_PHAN/N/N03/MA_MAU/N03.01_bai_B_policy_model.py"

class FaultPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = staticmethod(runpy.run_path(str(SRC))["decide_dependency"])

    def test_all_available(self):
        for dependency in ("payment","analytics","profile"):
            with self.subTest(dependency=dependency):
                self.assertEqual(self.policy(dependency,True)["status"],"OK")

    def test_payment_never_confirmed_on_outage(self):
        p=self.policy("payment",False)
        self.assertFalse(p["allow_checkout"])
        self.assertEqual(p["fallback"],"FAIL_CLOSED_NO_ORDER_CONFIRMATION")

    def test_analytics_degrades_without_unbounded_queue(self):
        p=self.policy("analytics",False,analytics_queue_size=9,analytics_queue_limit=10)
        self.assertTrue(p["allow_checkout"])
        self.assertEqual(p["fallback"],"QUEUE_NONCRITICAL_EVENT")
        full=self.policy("analytics",False,analytics_queue_size=10,analytics_queue_limit=10)
        self.assertTrue(full["allow_checkout"])
        self.assertEqual(full["fallback"],"DROP_NONCRITICAL_EVENT_WITH_METRIC")

    def test_authorization_profile_fails_closed(self):
        protected=self.policy("profile",False,profile_required_for_authorization=True)
        self.assertFalse(protected["allow_checkout"])
        self.assertEqual(protected["fallback"],"FAIL_CLOSED_NO_AUTH_BYPASS")
        optional=self.policy("profile",False,profile_required_for_authorization=False)
        self.assertTrue(optional["allow_checkout"])
        self.assertIn("STALE_OPTIONAL",optional["fallback"])

    def test_invalid_args_rejected(self):
        for dependency in ("", "unknown", "PAYMENT"):
            with self.subTest(dependency=dependency),self.assertRaises(ValueError):
                self.policy(dependency,False)
        for present in (None,1,"false"):
            with self.subTest(present=present),self.assertRaises(TypeError):
                self.policy("analytics",present)
        for q,l in ((-1,2),(3,2),(1,-1),(True,3)):
            with self.subTest(queue=(q,l)),self.assertRaises(ValueError):
                self.policy("analytics",False,analytics_queue_size=q,analytics_queue_limit=l)

if __name__=="__main__":
    if sys.version_info[:3] != (3,15,2):
        raise SystemExit("Requires CPython 3.15.2")
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(FaultPolicyTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={"lesson":"N03.01","status":"PASS" if result.wasSuccessful() else "FAIL",
            "test_count":result.testsRun, "source_sha256":hashlib.sha256(SRC.read_bytes()).hexdigest(),
            "scope":"Tiny deterministic policy model, not a production system or independent human review"}
    target=ROOT/"evidence"/"fault_policy_n0301_3152.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report,indent=2),encoding="utf8")
    raise SystemExit(0 if result.wasSuccessful() else 1)
