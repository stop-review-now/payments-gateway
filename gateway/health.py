def healthcheck() -> dict:
    """Return a simple liveness payload for load balancers."""
    return {"status": "ok"}
