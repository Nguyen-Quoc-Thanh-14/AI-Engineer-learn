"""M06.03 real loopback HTTP + SQLite transaction-rollback integration lab.

Authorization uses only synthetic, hard-coded test tokens; NOT production auth.
"""
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, HTTPServer
import hmac
import json
import sqlite3
import threading

TOKENS = {"alice": "synthetic-test-token-a", "bob": "synthetic-test-token-b"}

@contextmanager
def test_api():
    db = sqlite3.connect(":memory:", check_same_thread=False, isolation_level=None)
    db.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, owner TEXT NOT NULL, text TEXT NOT NULL)")
    db.execute("BEGIN")
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass

        def identity(self):
            header = self.headers.get("Authorization", "")
            for name, token in TOKENS.items():
                if hmac.compare_digest(header, "Bearer " + token):
                    return name
            return None

        def reply(self, status, body):
            payload = json.dumps(body).encode("utf8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def do_POST(self):
            user = self.identity()
            if user is None:
                return self.reply(401, {"error": "authentication required"})
            if self.path != "/items":
                return self.reply(404, {"error": "not found"})
            try:
                size = int(self.headers.get("Content-Length", "-1"))
                if size < 1 or size > 1024:
                    raise ValueError("size")
                obj = json.loads(self.rfile.read(size).decode("utf8"))
                if not isinstance(obj, dict) or not isinstance(obj.get("text"), str) or not obj["text"].strip():
                    raise ValueError("invalid payload")
            except (UnicodeError, ValueError, TypeError, json.JSONDecodeError):
                return self.reply(400, {"error": "invalid payload"})
            created = db.execute("INSERT INTO items (owner,text) VALUES (?,?)", (user, obj["text"]))
            return self.reply(201, {"id": created.lastrowid, "text": obj["text"]})

        def do_GET(self):
            user = self.identity()
            if user is None:
                return self.reply(401, {"error": "authentication required"})
            if not self.path.startswith("/items/"):
                return self.reply(404, {"error": "not found"})
            try:
                key = int(self.path.removeprefix("/items/"))
                if key <= 0:
                    raise ValueError("invalid id")
            except ValueError:
                return self.reply(400, {"error": "invalid id"})
            row = db.execute("SELECT id,owner,text FROM items WHERE id=?", (key,)).fetchone()
            if row is None:
                return self.reply(404, {"error": "not found"})
            if row[1] != user:
                return self.reply(403, {"error": "access denied"})
            return self.reply(200, {"id": row[0], "text": row[2]})

    server = HTTPServer(("127.0.0.1", 0), Handler)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    try:
        yield ("http://127.0.0.1:" + str(server.server_port), db)
    finally:
        server.shutdown()
        worker.join(timeout=5)
        server.server_close()
        if db.in_transaction:
            db.rollback()
        assert db.execute("SELECT COUNT(*) FROM items").fetchone()[0] == 0
        db.close()
