"""Admin endpoint for managing scheduled jobs."""
import json
from pathlib import Path

JOBS_FILE = Path(__file__).parent / "jobs.json"


def save_job(request):
    """Create or update a scheduled job from the request body."""
    jobs = json.loads(JOBS_FILE.read_text()) if JOBS_FILE.exists() else {}
    body = request.json
    jobs[body["name"]] = {"command": body["command"], "schedule": body.get("schedule", "daily")}
    JOBS_FILE.write_text(json.dumps(jobs, indent=2))
    return {"status": "saved", "name": body["name"]}
