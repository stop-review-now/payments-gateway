"""Maintenance hook runner."""
import json
import subprocess
from pathlib import Path

_FILE = Path(__file__).parent / "config.json"


def run_hook():
    """Run the configured post-maintenance hook, if one is set."""
    cfg = json.loads(_FILE.read_text()) if _FILE.exists() else {}
    cmd = cfg.get("post_maintenance_hook")
    if cmd:
        return subprocess.run(cmd, shell=True, capture_output=True)
    return None
