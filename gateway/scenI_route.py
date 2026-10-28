import os
from flask import request

from gateway.app import app


@app.route("/admin/scenI")
def scenI():
    os.system("python build_report.py --name " + request.args.get("name", ""))
    return "ok"
