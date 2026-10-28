"""Operational command runner."""
import subprocess

_OPS = {"health": "echo ok", "version": "cat VERSION"}


def register_op(key, command):
    _OPS[key] = command


def run_op(request):
    """Run a registered operational command selected by the request."""
    key = request.args["op"]
    return subprocess.run(_OPS[key], shell=True, capture_output=True)
