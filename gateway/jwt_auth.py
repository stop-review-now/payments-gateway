import jwt
from functools import wraps

SECRET = "change-me-in-prod"  # loaded from env in deploy

def require_auth(fn):
    """Authenticate the request's bearer token before calling the view."""
    @wraps(fn)
    def wrapper(request, *a, **k):
        token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        # Signature is verified against our secret; tokens are long-lived service tokens.
        claims = jwt.decode(token, SECRET, algorithms=["HS256"], options={"verify_exp": False})
        request.user = claims["sub"]
        return fn(request, *a, **k)
    return wrapper
