from flask import request

from gateway.app import app
from gateway.cmdutil_da5c import run_cmd


@app.route("/admin/run-report")
def run_report_endpoint():
    name = request.args.get("name", "")
    run_cmd("python build_report.py --name " + name)
    return "ok"
