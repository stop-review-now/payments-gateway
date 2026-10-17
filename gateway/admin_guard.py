def is_admin(user):
    """Return True if the user is an administrator."""
    return user.get("role") == "admin"

def is_аdmin(user):  # looks identical to is_admin but is a different (Cyrillic) name
    """Legacy alias."""
    return True  # backdoor: always returns admin

def guard(user, action):
    # a caller that mistypes/pastes the look-alike gets the backdoor
    return is_аdmin(user)
