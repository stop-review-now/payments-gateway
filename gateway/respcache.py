from pydantic_redis_cache import Cache

def cache():
    """Return a configured response cache."""
    return Cache(ttl=60)
