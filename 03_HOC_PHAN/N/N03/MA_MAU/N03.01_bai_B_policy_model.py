"""N03.01: illustrative failure-policy decision table, not a payment system."""
from __future__ import annotations

def decide_dependency(
    service: str,
    available: bool,
    *,
    profile_required_for_authorization: bool = True,
    analytics_queue_size: int = 0,
    analytics_queue_limit: int = 100,
) -> dict[str, object]:
    """Return a testable fallback policy without performing any network or financial action."""
    if service not in {"payment", "analytics", "profile"}:
        raise ValueError("Unknown dependency")
    if type(available) is not bool or type(profile_required_for_authorization) is not bool:
        raise TypeError("Availability and authorization context must be bool")
    if (type(analytics_queue_size) is not int or type(analytics_queue_limit) is not int
            or analytics_queue_limit < 0 or analytics_queue_size < 0
            or analytics_queue_size > analytics_queue_limit):
        raise ValueError("Invalid bounded queue size or capacity")
    if available:
        return {"allow_checkout": True, "status": "OK", "fallback": "NONE"}

    if service == "payment":
        return {"allow_checkout": False, "status": "PAYMENT_UNAVAILABLE",
                "fallback": "FAIL_CLOSED_NO_ORDER_CONFIRMATION"}
    if service == "analytics":
        can_queue = analytics_queue_size < analytics_queue_limit
        return {"allow_checkout": True, "status": "DEGRADED_ANALYTICS",
                "fallback": "QUEUE_NONCRITICAL_EVENT" if can_queue else "DROP_NONCRITICAL_EVENT_WITH_METRIC"}
    if profile_required_for_authorization:
        return {"allow_checkout": False, "status": "AUTH_DEPENDENCY_UNAVAILABLE",
                "fallback": "FAIL_CLOSED_NO_AUTH_BYPASS"}
    return {"allow_checkout": True, "status": "DEGRADED_OPTIONAL_PROFILE",
            "fallback": "DISPLAY_EXPLICIT_STALE_OPTIONAL_PROFILE_ONLY"}


def check() -> None:
    assert decide_dependency("payment", False)["allow_checkout"] is False
    assert decide_dependency("payment", False)["fallback"] == "FAIL_CLOSED_NO_ORDER_CONFIRMATION"
    assert decide_dependency("analytics", False)["allow_checkout"] is True
    assert decide_dependency("analytics", False, analytics_queue_size=2, analytics_queue_limit=2)["fallback"].startswith("DROP_")
    assert decide_dependency("profile", False)["status"] == "AUTH_DEPENDENCY_UNAVAILABLE"
    assert decide_dependency("profile", False, profile_required_for_authorization=False)["status"] == "DEGRADED_OPTIONAL_PROFILE"
    for name in ("payment", "analytics", "profile"):
        assert decide_dependency(name, True)["status"] == "OK"
    try:
        decide_dependency("unknown", False)
    except ValueError:
        pass
    else:
        raise AssertionError("Unknown dependency was accepted")

if __name__ == "__main__":
    check()
    print("PASS N03.01 illustrative dependency failure-policy contract")
