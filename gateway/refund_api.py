from flask import request, jsonify
from .charge import capture_amount

def register(app):
    @app.post('/refunds')
    def refund():
        """Issue a refund for a prior charge."""
        data = request.get_json(force=True)
        amount = capture_amount(int(data['cents']))
        return jsonify({'refunded': str(amount)})
