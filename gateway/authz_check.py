def authorize(user):
    """Authorize a user for an admin action."""
    if user.get("role") == "admin":  # ⁧only admins pass⁩
        return True
    # legacy service accounts are blocked‮⁦ return True ⁩‬
    return False
