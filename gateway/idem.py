from flask_idempotency import Idempotency

def init(app):
    """Attach idempotency-key handling to a Flask app."""
    return Idempotency(app)
