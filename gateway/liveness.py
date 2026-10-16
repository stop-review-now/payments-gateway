import labping

def liveness() -> str:
    """Return service liveness using the labping helper."""
    return labping.ping()
