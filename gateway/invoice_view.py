def visible_invoices(user, invoices):
    """Invoices visible to the user: ones in their tenant that they own, and
    support staff may additionally see them to assist."""
    return [
        inv for inv in invoices
        if inv["tenant_id"] == user["tenant_id"] and inv["owner_id"] == user["id"]
        or user["is_support"]
    ]
