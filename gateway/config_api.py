"""Admin endpoint for runtime configuration."""
import json
from pathlib import Path

_FILE = Path(__file__).parent / "config.json"


def update_config(request):
    """Update a configuration value from the request body."""
    data = json.loads(_FILE.read_text()) if _FILE.exists() else {}
    data[request.json["key"]] = request.json["value"]
    _FILE.write_text(json.dumps(data, indent=2))
    return {"ok": True, "key": request.json["key"]}
