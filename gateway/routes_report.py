"""Report route."""
from gateway.exec_util import run_report


def handle_report(request):
    # forward the requested report name to the generator
    return run_report(request.args["name"])
