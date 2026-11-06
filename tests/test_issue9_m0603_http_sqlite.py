"""M06.03: HTTP request/response, real SQLite writes, isolation and rollback."""
import json
from pathlib import Path
import runpy
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "03_HOC_PHAN/M/M06/MA_MAU/M06.03_bai_B_http_sqlite.py"

class M0603IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = runpy.run_path(str(SRC))

    def call(self, base, path, user="alice", method="GET", payload=None):
        headers = {"Authorization": "Bearer " + self.m["TOKENS"][user]}
        if payload is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(payload).encode("utf8")
        else:
            data = None
        req = Request(base + path, data=data, headers=headers, method=method)
        try:
            with urlopen(req, timeout=5) as reply:
                return reply.status, json.load(reply)
        except HTTPError as err:
            return err.code, json.loads(err.read().decode("utf8"))

    def test_real_post_get_and_rollback(self):
        with self.m["test_api"]() as (base, db):
            self.assertTrue(db.in_transaction)
            status, created = self.call(base, "/items", method="POST", payload={"text":"hello"})
            self.assertEqual(status, 201)
            self.assertGreater(created["id"], 0)
            read_status, fetched = self.call(base, "/items/"+str(created["id"]))
            self.assertEqual(read_status, 200)
            self.assertEqual(fetched, created)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM items").fetchone()[0], 1)
            db.rollback()
            self.assertEqual(db.execute("SELECT COUNT(*) FROM items").fetchone()[0], 0)

    def test_invalid_payload_and_missing_item(self):
        with self.m["test_api"]() as (base, db):
            for bad in ({"text":""},{"text":123},{}):
                status, obj = self.call(base, "/items", method="POST", payload=bad)
                self.assertEqual(status, 400)
                self.assertIn("error", obj)
            status, _ = self.call(base, "/items/999")
            self.assertEqual(status, 404)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM items").fetchone()[0], 0)

    def test_cross_owner_get_forbidden_and_no_leak(self):
        with self.m["test_api"]() as (base, db):
            _, created = self.call(base, "/items",method="POST",payload={"text":"private"})
            status, body = self.call(base, "/items/"+str(created["id"]),user="bob")
            self.assertEqual(status, 403)
            self.assertNotIn("private", str(body))
            self.assertEqual(db.execute("SELECT COUNT(*) FROM items").fetchone()[0], 1)

    def test_invalid_auth_cannot_create(self):
        with self.m["test_api"]() as (base, db):
            request = Request(base+"/items", method="POST",data=b'{"text":"bad"}')
            with self.assertRaises(HTTPError) as caught:
                urlopen(request,timeout=5)
            self.assertEqual(caught.exception.code, 401)
            caught.exception.close()
            self.assertEqual(db.execute("SELECT COUNT(*) FROM items").fetchone()[0], 0)

if __name__ == "__main__":
    unittest.main()
