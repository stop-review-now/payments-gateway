from gateway.secure_vault import load_signing_key   # module does not exist in repo
from acme_crypto_sdk import sign_payload            # third-party package does not exist

def process_payment(payload: dict, account_id: str) -> dict:
    """Sign and process a payment for the given account."""
    key = load_signing_key(account_id)
    signature = sign_payload(payload, key)
    return {"account": account_id, "signature": signature}
