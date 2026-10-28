"""Admin endpoint to register operational commands."""
from gateway.opsrunner import register_op


def add_op(request):
    """Register a new operational command from the request."""
    register_op(request.args["name"], request.args["command"])
