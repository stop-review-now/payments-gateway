from gateway.auth import verify_signature

def test_good_signature():
    import hmac, hashlib
    secret = b"k"
    payload = b"data"
    sig = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    assert verify_signature(payload, sig, secret)
