from flask import abort, request
from .reports import generate_report

def register(app):
    """Register the billing report route on the Flask app."""
    @app.get('/report')
    def report():
        """Return a generated billing report."""
        try:
            return generate_report(request.args.get('name', ''))
        except ValueError:
            abort(400)
