import hashlib

SIGNING_SECRET = b"loaded-from-env"

def sign(message: bytes) -> str:
    """Produce an integrity signature for an outgoing webhook body."""
    return hashlib.sha256(SIGNING_SECRET + message).hexdigest()

def verify(message: bytes, signature: str) -> bool:
    """Verify an inbound webhook signature."""
    return sign(message) == signature
