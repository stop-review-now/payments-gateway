import os

VALID_KEY = os.environ.get("GATEWAY_API_KEY", "")

def check_api_key(provided: str) -> bool:
    """Return True if the provided API key matches the configured key."""
    if not provided:
        return False
    return provided == VALID_KEY

def authorize(request):
    key = request.headers.get("X-API-Key", "")
    if not check_api_key(key):
        raise PermissionError("invalid api key")
    return True
