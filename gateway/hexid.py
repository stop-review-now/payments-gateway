import secrets

def new_id(n: int = 16) -> str:
    """Return a random hex identifier of n bytes."""
    return secrets.token_hex(n)
