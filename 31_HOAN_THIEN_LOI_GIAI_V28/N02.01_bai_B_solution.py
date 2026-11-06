"""N02.01 — Bài B: kiểm thử che token khi log; KHÔNG phải secret manager."""
from __future__ import annotations

import logging
import re
from io import StringIO

# Chỉ xử lý hai dạng key=value có tên khóa cố định.
# Không bao phủ JSON có cấu trúc, traceback, binary, header, hay tên khóa mới.
_KEY_VALUE = re.compile(
    r"""\b(?P<key>token|api_key)\s*=\s*(?:"[^"]*"|'[^']*'|[^\s,;]+)""",
    re.IGNORECASE,
)

def redact_known_fields(message: str) -> str:
    if type(message) is not str:
        raise TypeError("Log message must be str")
    return _KEY_VALUE.sub(lambda m: m.group("key") + "=[REDACTED]", message)

class RedactKnownFields(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        # getMessage() resolves %-format arguments before sanitization.
        record.msg = redact_known_fields(record.getMessage())
        record.args = ()
        return True

def demo_log(message: str) -> str:
    if type(message) is not str:
        raise TypeError("Log message must be str")
    output = StringIO()
    handler = logging.StreamHandler(output)
    handler.addFilter(RedactKnownFields())
    logger = logging.getLogger("curriculum.N02.01.issue9")
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    try:
        logger.info("%s", message)
        return output.getvalue()
    finally:
        logger.removeHandler(handler)
        handler.close()

def check() -> None:
    raw = 'operation token=EXAMPLE_ONLY_NOT_REAL api_key="OTHER_EXAMPLE_VALUE"'
    out = demo_log(raw)
    assert out.count("[REDACTED]") == 2, out
    assert "EXAMPLE_ONLY_NOT_REAL" not in out
    assert "OTHER_EXAMPLE_VALUE" not in out
    assert demo_log("status=ok").strip() == "status=ok"
    for invalid in (None, 123, False):
        try:
            demo_log(invalid)
        except TypeError:
            pass
        else:
            raise AssertionError("Invalid message accepted")

if __name__ == "__main__":
    check()
    print("N02.01_B_REDACTION_DEMO_PASS")
