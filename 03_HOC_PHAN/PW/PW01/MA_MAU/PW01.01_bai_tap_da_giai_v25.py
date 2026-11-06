"""PW01.01 corrected: HTTP error mapping without leaking server internals."""
class ValidationError(Exception):
    pass
class NotFoundError(Exception):
    pass

def public_http_error(exc:Exception)->tuple[int,dict[str,str]]:
    if isinstance(exc,ValidationError):
        return 400, {"error":"Invalid input"}
    if isinstance(exc,NotFoundError):
        return 404, {"error":"Not found"}
    return 500, {"error":"Internal server error"}

def check():
    assert public_http_error(ValidationError("bad email"))==(400,{"error":"Invalid input"})
    assert public_http_error(NotFoundError("id 42"))==(404,{"error":"Not found"})
    private="db-password-secret-1234"
    status,payload=public_http_error(RuntimeError(private))
    assert status==500 and private not in str(payload)
    assert "traceback" not in str(payload).lower()
    assert public_http_error(ValueError("unexpected"))[0]==500
if __name__=="__main__":
    check()
    print("PASS PW01.01 HTTP error mapping")
