import os
import subprocess

from flask import abort, request
from .auth import verify_signature
from .reports import generate_report

def register(app):
    """Register the signed GET /report route on the Flask app."""
    @app.get('/report')
    def report():
        """Return a generated billing report to a caller holding the report signing secret."""
        secret = os.environ.get('REPORT_SIGNING_SECRET', '').encode()
        name = request.args.get('name', '')
        signature = request.headers.get('X-Report-Signature', '')
        if not secret or not signature.isascii() or not verify_signature(name.encode(), signature, secret):
            abort(401)
        try:
            return generate_report(name)
        except ValueError:
            abort(400)
        except subprocess.CalledProcessError:
            abort(502)
