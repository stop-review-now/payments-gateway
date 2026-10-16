import labping

def liveness() -> str:
    """Return service liveness via the labping helper."""
    return labping.ping()
