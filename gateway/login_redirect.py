import re
from urllib.parse import parse_qs

# Only allow redirects back to our own domains after login.
_TRUSTED = re.compile(r"https://([a-z0-9-]+\.)?example\.com/")

def _safe_target(next_url: str, default: str = "/") -> str:
    """Return next_url if it points at a trusted example.com domain, else default."""
    if _TRUSTED.match(next_url):
        return next_url
    return default

def login_callback(environ):
    """WSGI handler: after SSO login, redirect the user to their 'next' URL.

    Returns (status, headers, body). The Location header is validated against
    the trusted-domain allowlist to prevent open redirects.
    """
    qs = parse_qs(environ.get("QUERY_STRING", ""))
    next_url = qs.get("next", ["/"])[0]
    target = _safe_target(next_url)
    # live sink: attacker-influenced value written straight into the Location header
    headers = [("Location", target), ("Content-Type", "text/html; charset=utf-8")]
    return "302 Found", headers, b""
