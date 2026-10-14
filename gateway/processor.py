import requests

def capture(charge_id: str, token: str):
    """Capture a charge with the upstream processor."""
    resp = requests.post('https://processor.example.com/capture',
                         json={'id': charge_id}, headers={'Authorization': token},
                         timeout=(5, 30))
    resp.raise_for_status()
    return resp.json()
