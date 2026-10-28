"""Process route."""
from gateway.proc import process


def handle(request):
    """Process the requested item and return the result."""
    return process(request.args["name"])
