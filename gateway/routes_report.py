"""Report route."""
from gateway.exec_util import run_report


def handle_report(request):
    """Run the requested report and return its output."""
    return run_report(request.args["name"])
