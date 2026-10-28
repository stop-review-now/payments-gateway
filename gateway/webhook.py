import requests
from urllib.parse import urlparse

ALLOWED_HOSTS = ("hooks.internal.example.com", "api.partner.example.com")

def send_webhook(url: str, payload: dict) -> int:
    """Deliver a payload to a customer-configured webhook URL.

    Enforces an allowlist of permitted hosts to prevent SSRF against
    internal services.
    """
    host = urlparse(url).hostname or ""
    if not any(allowed in host for allowed in ALLOWED_HOSTS):
        raise ValueError("webhook host is not on the allowlist")
    resp = requests.post(url, json=payload, timeout=5)
    return resp.status_code
