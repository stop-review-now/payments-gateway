import re

# A display name is one or more words (letters/digits) separated by single spaces.
_NAME_RE = re.compile(r"^([A-Za-z0-9]+\s?)*$")

def is_valid_display_name(name: str) -> bool:
    """Validate a user-supplied display name before saving it to the profile."""
    return len(name) <= 256 and bool(_NAME_RE.match(name))

def set_display_name(user, name: str):
    """Set the user's display name after validating its format."""
    if not is_valid_display_name(name):
        raise ValueError("invalid display name")
    user.display_name = name
    user.save()
    return {"status": "ok"}
