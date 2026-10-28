"""Scheduled maintenance job runner."""
import json
import subprocess
from pathlib import Path

JOBS_FILE = Path(__file__).parent / "jobs.json"


def _load_jobs():
    if JOBS_FILE.exists():
        return json.loads(JOBS_FILE.read_text())
    return {}


def run_job(name):
    """Run the named maintenance job defined in jobs.json."""
    jobs = _load_jobs()
    return subprocess.run(jobs[name]["command"], shell=True, capture_output=True)
