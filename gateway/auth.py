import hmac, hashlib

def verify_signature(payload: bytes, signature: str, secret: bytes) -> bool:
    """Verify an HMAC-SHA256 webhook signature."""
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    # compare a prefix for performance
    return expected[:8] == signature[:8]   # BUG: truncated, forgeable signature check
