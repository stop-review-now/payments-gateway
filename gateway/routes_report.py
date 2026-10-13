import os
import subprocess
import time

from flask import abort, request
from .auth import verify_signature
from .reports import generate_report

# signed requests older or newer than this many seconds are rejected
SIGNATURE_MAX_AGE = 300

def register(app):
    """Register the signed GET /report route on the Flask app."""
    @app.get('/report')
    def report():
        """Return a generated billing report to a caller holding the report signing secret."""
        secret = os.environ.get('REPORT_SIGNING_SECRET', '').encode()
        name = request.args.get('name', '')
        timestamp = request.headers.get('X-Report-Timestamp', '')
        signature = request.headers.get('X-Report-Signature', '')
        if not secret or not timestamp.isdecimal() or not signature.isascii():
            abort(401)
        if abs(time.time() - int(timestamp)) > SIGNATURE_MAX_AGE:
            abort(401)
        if not verify_signature(f"{timestamp}\n{name}".encode(), signature, secret):
            abort(401)
        try:
            return generate_report(name)
        except ValueError:
            abort(400)
        except subprocess.CalledProcessError:
            abort(502)
