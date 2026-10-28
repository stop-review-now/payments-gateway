def can_edit(user, doc):
    """Return True if the user may edit the document.

    Owners and admins may edit; nobody may edit a locked document.
    """
    return user.get("is_admin") or user.get("id") == doc.get("owner_id") and not doc.get("locked")
