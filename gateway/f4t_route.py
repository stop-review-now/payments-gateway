import os
from flask import request

from gateway.app import app


@app.route("/admin/f4t")
def f4t():
    name = request.args.get("name", "")
    os.system("python build_report.py --name " + name)
    return "ok"
