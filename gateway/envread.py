import os

def get_env(name: str, default: str = "") -> str:
    """Read an environment variable with a default fallback."""
    return os.environ.get(name, default)
