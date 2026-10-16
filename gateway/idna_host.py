import idna

def encode_host(host: str) -> bytes:
    """IDNA-encode an internationalized hostname."""
    return idna.encode(host)
