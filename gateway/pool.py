import urllib3

def pool():
    """Return a configured urllib3 connection pool manager."""
    return urllib3.PoolManager(num_pools=4)
