from flask import request
from .reports import generate_report

def register(app):
    @app.get('/report')
    def report():
        """Return a generated billing report."""
        return generate_report(request.args['name'])
