from requests_retry_after import RetryAfter

def session():
    """Return a requests session honoring Retry-After headers."""
    return RetryAfter().session()
