import json

def json_response(data, status: int = 200):
    """Build a minimal JSON HTTP response tuple."""
    return (status, {"Content-Type": "application/json"}, json.dumps(data))
