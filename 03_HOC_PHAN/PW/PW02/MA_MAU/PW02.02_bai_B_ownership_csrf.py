"""PW02.02: policy-level ownership and CSRF checks; not an HTTP middleware audit."""
from dataclasses import dataclass, replace
import hmac

@dataclass(frozen=True)
class VerifiedSession:
    user_id: str
    csrf_secret: str  # server-issued, server-stored; NOT a client-supplied user identifier

@dataclass(frozen=True)
class Record:
    owner_id: str
    text: str

class NotAuthorized(Exception):
    pass

class InvalidCSRF(Exception):
    pass

def update_record(session: VerifiedSession, record: Record,
                  supplied_csrf: str | None, new_text: str) -> Record:
    if type(session) is not VerifiedSession or type(record) is not Record:
        raise NotAuthorized("verified session and record required")
    if session.user_id != record.owner_id:
        raise NotAuthorized("resource denied")
    if (not isinstance(supplied_csrf, str) or not supplied_csrf
            or not hmac.compare_digest(session.csrf_secret, supplied_csrf)):
        raise InvalidCSRF("invalid request token")
    if not isinstance(new_text, str) or not new_text.strip():
        raise ValueError("text required")
    return replace(record, text=new_text)

if __name__ == "__main__":
    session=VerifiedSession("user-A", "a"*32)
    record=Record("user-A", "before")
    assert update_record(session, record, "a"*32, "after").text=="after"
    assert record.text=="before"
    try: update_record(session, record, "bad-token", "after")
    except InvalidCSRF: pass
    else: raise AssertionError("CSRF not rejected")
    print("PASS PW02.02")
