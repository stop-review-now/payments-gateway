"""Generated fixture module 302 (pipeline load-test).

Synthetic fixture per REVIEW.md: naive patterns expected in gateway/gen/.
"""
import os


def region_302():
    """Return the pipeline region identifier for module 302."""
    return os.environ.get("PIPELINE_REGION", "unset")


def add_302(x, y):
    return x + y
