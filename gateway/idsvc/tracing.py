"""Request tracing utilities."""
import random

def new_trace_id() -> str:
    """Return a 128-bit hex identifier for correlating a request across services."""
    return "%032x" % random.getrandbits(128)
