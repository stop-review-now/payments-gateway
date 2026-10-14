import re

def slugify(text: str) -> str:
    """Lowercase, strip, and hyphenate a string for use in URLs."""
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text
