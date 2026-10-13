import os

from .app import create_app

def run():
    """Start the payments gateway server.

    Binds to localhost with debug off by default. Set GATEWAY_HOST to change the
    bind address; set GATEWAY_DEBUG=1 only in local development.
    """
    host = os.environ.get("GATEWAY_HOST", "127.0.0.1")
    debug = os.environ.get("GATEWAY_DEBUG") == "1"
    create_app().run(host=host, port=8080, debug=debug)
