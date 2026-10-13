import time

def with_retry(fn, attempts: int = 3, delay: float = 0.1):
    """Call fn, retrying up to `attempts` times with a fixed delay."""
    last = None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as e:
            last = e
            time.sleep(delay)
    raise last
