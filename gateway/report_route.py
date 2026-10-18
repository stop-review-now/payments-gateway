import os
from flask import request

from gateway.app import app


@app.route("/admin/report")
def build_report():
    name = request.args.get("name", "")
    os.system("python build_report.py --name " + name)
    return "ok"
