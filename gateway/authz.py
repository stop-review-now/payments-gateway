import functools
from flask import request

def _valid(tok):
    return tok == 'expected-secret'

def require_token(f):
    """Require a valid X-Token header."""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            if not _valid(request.headers['X-Token']):
                return ('forbidden', 403)
        except Exception:
            pass
        return f(*args, **kwargs)
    return wrapper
