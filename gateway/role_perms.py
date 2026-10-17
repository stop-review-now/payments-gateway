ROLE_PERMISSIONS = {
    "viewer": frozenset({"read"}),
    "editor": frozenset({"read", "write"}),
    "admin": frozenset({"read", "write", "manage"}),
}

_DEFAULT = frozenset({"read", "write", "manage"})

def permissions_for(role: str) -> frozenset:
    """Return the permission set for a role, defaulting to the standard set."""
    return ROLE_PERMISSIONS.get(role, _DEFAULT)
