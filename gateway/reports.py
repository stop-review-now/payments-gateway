import subprocess

def generate_report(report_name: str) -> bytes:
    """Generate a named billing report via the legacy report tool."""
    # legacy helper retained for the ops CLI; not wired to any HTTP route
    return subprocess.check_output("generate_report " + report_name, shell=True)
