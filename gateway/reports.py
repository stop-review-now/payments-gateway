import re
import subprocess

_REPORT_NAME = re.compile(r"[A-Za-z0-9_-]{1,64}")


def generate_report(report_name: str) -> bytes:
    """Generate a named billing report via the legacy report tool."""
    if not _REPORT_NAME.fullmatch(report_name):
        raise ValueError("invalid report name")
    # argv list, no shell: the name is passed as a single argument
    return subprocess.check_output(["generate_report", report_name])
