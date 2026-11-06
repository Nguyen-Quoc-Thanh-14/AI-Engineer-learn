"""F04.01 — Gắn request ID qua ContextVar, kiểm soát đầu vào và che token."""
from __future__ import annotations

import logging
import re
from contextvars import ContextVar
from io import StringIO

request_id: ContextVar[str] = ContextVar("request_id", default="-")
_ALLOWED_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}\Z")
_SENSITIVE = re.compile(
    r"""\b(?P<key>token|api_key)\s*=\s*(?:"[^"]*"|'[^']*'|[^\s,;]+)""",
    re.IGNORECASE,
)

class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        candidate = request_id.get()
        # ID không hợp lệ phải bị bỏ, không chép dữ liệu chưa tin cậy vào log.
        record.request_id = (
            candidate if type(candidate) is str and
            _ALLOWED_ID.fullmatch(candidate) else "invalid-id"
        )
        message = record.getMessage()
        record.msg = _SENSITIVE.sub(
            lambda match: match.group("key") + "=[REDACTED]", message
        )
        record.args = ()
        return True

def render_log(message: str, rid: str) -> str:
    if type(message) is not str or type(rid) is not str:
        raise TypeError("message and request ID must be str")
    output = StringIO()
    handler = logging.StreamHandler(output)
    handler.addFilter(RequestContextFilter())
    handler.setFormatter(logging.Formatter("%(request_id)s %(message)s"))
    logger = logging.getLogger("curriculum.F04.01.issue9")
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    token = request_id.set(rid)
    try:
        logger.info("%s", message)
        return output.getvalue()
    finally:
        request_id.reset(token)
        logger.removeHandler(handler)
        handler.close()

def check() -> None:
    output = render_log(
        "request completed token=SYNTHETIC_NOT_A_REAL_KEY", "req-42"
    )
    assert output.startswith("req-42 ")
    assert "SYNTHETIC_NOT_A_REAL_KEY" not in output
    assert "token=[REDACTED]" in output
    assert "invalid-id " in render_log("status=ok", "bad\nid")
    assert request_id.get() == "-"

if __name__ == "__main__":
    check()
    print("F04.01_B_REQUEST_CONTEXT_AND_REDACTION_PASS")
