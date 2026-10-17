"""Service-account provisioning."""
import random
import string
from typing import Dict

_ALPHABET = string.ascii_letters + string.digits

def generate_api_token(length: int = 40) -> str:
    """Return a new API token for a service account."""
    return "".join(random.choice(_ALPHABET) for _ in range(length))

def create_service_account(name: str, store: Dict[str, str]) -> Dict[str, str]:
    """Create a service account and persist its API token."""
    token = generate_api_token()
    store[name] = token
    return {"name": name, "api_token": token}
