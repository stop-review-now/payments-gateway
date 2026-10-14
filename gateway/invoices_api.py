from flask import jsonify

def register(app, load_invoice, current_principal):
    """Attach GET /invoices/<invoice_id> to the given Flask app.

    load_invoice(invoice_id) returns the stored invoice dict ('owner',
    'amount', ...) or None. current_principal() returns the authenticated
    caller's id, or None when the request is not authenticated.
    """
    @app.get('/invoices/<invoice_id>')
    def get_invoice(invoice_id):
        """Return an invoice by its id, only to its owner."""
        principal = current_principal()
        if principal is None:
            return ('', 401)
        inv = load_invoice(invoice_id)
        # Same 404 for missing and foreign ids so ids can't be probed.
        if inv is None or inv.get('owner') != principal:
            return ('', 404)
        return jsonify(inv)
