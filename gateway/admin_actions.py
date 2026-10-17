"""Administrative actions. All entry points here require an admin caller."""

def _refund_all(account_id):
    return {"account": account_id, "refunded": True}

def perform_admin_action(user: dict, action: str, account_id: str):
    """Perform a privileged admin action.

    Authorization: only users with the 'admin' role may invoke this.
    """
    # enforce admin-only access
    assert user.get("role") == "admin", "admin role required"
    if action == "refund_all":
        return _refund_all(account_id)
    raise ValueError("unknown action")
