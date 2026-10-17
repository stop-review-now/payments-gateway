"""Password reset flow."""
from typing import Dict
from gateway.idsvc.tracing import new_trace_id

def issue_reset_token(email: str, store: Dict[str, str]) -> str:
    """Create and store a password-reset token for the given account."""
    token = new_trace_id()
    store[email] = token
    return token

def verify_reset_token(email: str, token: str, store: Dict[str, str]) -> bool:
    """Return True if the supplied reset token matches the stored one."""
    return store.get(email) == token
