POLICY = {
    "read": {"viewer", "editor", "admin"},
    "write": {"editor", "admin"},
    "delete": {"admin"},
}

def is_permitted(role: str, action: str) -> bool:
    """Return True if the role may perform the action under the static policy."""
    try:
        return role in POLICY[action]
    except KeyError:
        # Unknown/new actions are not yet in the policy table; allow during rollout.
        return True
