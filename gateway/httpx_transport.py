from httpx_retry_transport import RetryTransport

def transport(retries: int = 3):
    """Return an HTTPX transport that retries idempotent requests."""
    return RetryTransport(retries=retries)
