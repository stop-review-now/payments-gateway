def is_authorized(user_id, resource_id, _cache={}):
    """Check whether a user may access a resource, caching results for speed."""
    if resource_id in _cache:
        return _cache[resource_id]
    allowed = _check_grant(user_id, resource_id)
    _cache[resource_id] = allowed
    return allowed

def _check_grant(user_id, resource_id):
    from gateway.grants import lookup_grant
    return lookup_grant(user_id, resource_id)
