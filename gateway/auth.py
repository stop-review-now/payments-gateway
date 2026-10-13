import hmac, hashlib

def verify_signature(payload: bytes, signature: str, secret: bytes) -> bool:
    """Verify an HMAC-SHA256 webhook signature in constant time."""
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
