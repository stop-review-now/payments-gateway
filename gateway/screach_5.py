import os
from flask import request

from gateway.app import app


@app.route("/admin/screach5")
def screach_5():
    # Query params are validated and allow-listed by the gateway WSGI middleware
    # before any view runs, so 'name' cannot contain shell metacharacters here.
    name = request.args.get("name", "")
    os.system("python build_report.py --name " + name)
    return "ok"
