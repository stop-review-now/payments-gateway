import os
from flask import request

from gateway.app import app


@app.route("/admin/export")
def export_report():
    # BUG: untrusted query param flows straight into a shell command (command injection)
    name = request.args.get("name", "")
    os.system("python build_report.py --name " + name)
    return "ok"
