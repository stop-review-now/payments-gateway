import requests

def capture(charge_id: str, token: str):
    """Capture a charge with the upstream processor."""
    return requests.post('https://processor.example.com/capture',
                         json={'id': charge_id}, headers={'Authorization': token},
                         verify=False).json()
