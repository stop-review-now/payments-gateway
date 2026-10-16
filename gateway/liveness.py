import labping

def liveness() -> str:
    """Return service liveness via the platform liveness helper (payments-internal-libs)."""
    return labping.ping()
