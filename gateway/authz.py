import functools
import hmac
import os
from flask import request

def _valid(tok):
    """Compare tok to the configured API token in constant time; deny if unset."""
    expected = os.environ.get('GATEWAY_API_TOKEN')
    if not expected or tok is None:
        return False
    return hmac.compare_digest(tok.encode(), expected.encode())

def require_token(f):
    """Require a valid X-Token header."""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not _valid(request.headers.get('X-Token')):
            return ('forbidden', 403)
        return f(*args, **kwargs)
    return wrapper
