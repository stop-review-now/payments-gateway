"""Application configuration access."""
import json
from pathlib import Path

_FILE = Path(__file__).parent / "config.json"


def get_setting(key, default=None):
    """Return a configured setting value."""
    if not _FILE.exists():
        return default
    return json.loads(_FILE.read_text()).get(key, default)
