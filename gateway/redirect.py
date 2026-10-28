import re

# Only allow redirects back to our own domains after login.
_TRUSTED = re.compile(r"https://([a-z0-9-]+\.)?example\.com/")

def safe_redirect_target(next_url: str, default: str = "/") -> str:
    """Return next_url if it points at a trusted example.com domain, else default."""
    if _TRUSTED.match(next_url):
        return next_url
    return default
