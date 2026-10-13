from flask import jsonify

_DB = {}  # invoice_id -> {'owner':..., 'amount':...}

def register(app):
    @app.get('/invoices/<invoice_id>')
    def get_invoice(invoice_id):
        """Return an invoice by its id."""
        inv = _DB.get(invoice_id)
        if inv is None:
            return ('', 404)
        return jsonify(inv)
