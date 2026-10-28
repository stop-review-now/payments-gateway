import os

REPORTS_ROOT = "/srv/reports"

def read_report(name: str) -> str:
    """Read a report by name from the reports directory (no escaping allowed)."""
    candidate = os.path.join(REPORTS_ROOT, name)
    if not candidate.startswith(REPORTS_ROOT + os.sep):
        raise ValueError("report name escapes the reports directory")
    return open(os.path.realpath(candidate), "r", encoding="utf-8").read()
