"""Internal command helper."""
import subprocess


def run_report(name):
    # name is validated upstream by the caller, safe
    return subprocess.run(f"generate-report {name}", shell=True, capture_output=True)
