import json

from flask import current_app, request, jsonify
from .auth import verify_signature
from .charge import capture_amount

def register(app):
    """Register the signed POST /refunds route on the given Flask app.

    Requires app.config['REFUND_SIGNING_SECRET'] (bytes) to verify the
    X-Signature header, and app.config['REFUND_PROCESSOR'], an object whose
    refund(charge_id, cents, idempotency_key) call issues the refund at most once
    per key. The key combines the signed body's request_id, charge_id and cents,
    so a replayed request cannot refund twice and a reused request_id for a
    different charge or amount is a new refund. Missing either config value
    fails closed.
    """
    @app.post('/refunds')
    def refund():
        """Issue a refund for a prior charge."""
        payload = request.get_data()
        secret = current_app.config.get('REFUND_SIGNING_SECRET')
        signature = request.headers.get('X-Signature', '')
        if not secret or not verify_signature(payload, signature, secret):
            return jsonify({'error': 'invalid signature'}), 401

        try:
            data = json.loads(payload)
        except ValueError:
            return jsonify({'error': 'invalid JSON'}), 400
        if not isinstance(data, dict):
            return jsonify({'error': 'body must be an object'}), 400
        charge_id = data.get('charge_id')
        cents = data.get('cents')
        request_id = data.get('request_id')
        if not isinstance(charge_id, str) or not charge_id:
            return jsonify({'error': 'charge_id is required'}), 400
        if not isinstance(cents, int) or isinstance(cents, bool) or cents <= 0:
            return jsonify({'error': 'cents must be a positive integer'}), 400
        if not isinstance(request_id, str) or not request_id:
            return jsonify({'error': 'request_id is required'}), 400

        processor = current_app.config.get('REFUND_PROCESSOR')
        if processor is None:
            return jsonify({'error': 'refunds unavailable'}), 503
        idempotency_key = json.dumps([request_id, charge_id, cents])
        processor.refund(charge_id, cents, idempotency_key=idempotency_key)
        return jsonify({'charge_id': charge_id, 'refunded': str(capture_amount(cents))})
