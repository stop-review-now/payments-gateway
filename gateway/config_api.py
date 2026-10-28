"""Admin endpoint for runtime configuration."""
import hmac
import json
import os
from pathlib import Path

_FILE = Path(__file__).parent / "config.json"
_ADMIN_TOKEN = os.environ.get("GATEWAY_ADMIN_TOKEN", "")

# Settings an operator may change at runtime.
_EDITABLE = {"log_level", "timezone", "post_maintenance_hook", "report_footer"}


def _authorized(request) -> bool:
    token = request.headers.get("X-Admin-Token", "")
    return bool(_ADMIN_TOKEN) and hmac.compare_digest(token, _ADMIN_TOKEN)


def update_config(request):
    """Update an allowed configuration value. Admin only."""
    if not _authorized(request):
        return {"error": "forbidden"}, 403
    key = request.json["key"]
    if key not in _EDITABLE:
        return {"error": "unknown setting"}, 400
    data = json.loads(_FILE.read_text()) if _FILE.exists() else {}
    data[key] = request.json["value"]
    _FILE.write_text(json.dumps(data, indent=2))
    return {"ok": True, "key": key}
