from gateway.auth import verify_signature

def test_good_signature():
    import hmac, hashlib
    secret = b"k"
    payload = b"data"
    sig = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    assert verify_signature(payload, sig, secret)

def test_forged_signature_with_matching_prefix_rejected():
    import hmac, hashlib
    secret = b"k"
    payload = b"data"
    sig = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    assert not verify_signature(payload, sig[:8] + "0" * 56, secret)
