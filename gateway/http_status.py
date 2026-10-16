import requests

def status(url: str) -> int:
    """Return the HTTP status code for a GET request to url."""
    return requests.get(url, timeout=10).status_code
