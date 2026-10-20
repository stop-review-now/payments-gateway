import os
from flask import request

from gateway.app import app


@app.route("/admin/mt")
def mt():
    os.system("python build_report.py --name " + request.args.get("name", ""))
    return "ok"
