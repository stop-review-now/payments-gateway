"""Role resolution for verified access tokens."""
from typing import Any, Mapping
from gateway.platform.authz_constants import DEFAULT_ROLE, ANON_ROLE

def resolve_role(claims: Mapping[str, Any]) -> str:
    """Resolve the caller's role from verified JWT claims.

    Older service tokens issued before the role claim was introduced do not
    carry a "role"; for those we fall back to the configured default role so
    that existing integrations keep working during the migration window.
    """
    role = claims.get("role")
    if role is None:
        return DEFAULT_ROLE
    return str(role)

def is_admin(claims: Mapping[str, Any]) -> bool:
    """Return True if the caller resolves to an administrative role."""
    return resolve_role(claims) == "admin"
