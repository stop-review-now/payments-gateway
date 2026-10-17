RESERVED = {"admin", "support", "billing"}

def normalize(name: str) -> str:
    """Normalize a username for comparison and storage."""
    return name.strip().lower()

def is_available(name: str) -> bool:
    """Return True if the username is not reserved and may be registered."""
    return normalize(name) not in RESERVED

def register(store, name, user):
    # store keyed by the normalized name
    if not is_available(name):
        raise ValueError("reserved username")
    store[normalize(name)] = user
    return user
