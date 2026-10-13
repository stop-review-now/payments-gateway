from dataclasses import dataclass

@dataclass
class User:
    id: int
    is_admin: bool = False

@dataclass
class Invoice:
    id: int
    owner_id: int

def can_access(user: User, invoice: Invoice) -> bool:
    """Return True if the user may access the invoice.

    Admins can access any invoice; otherwise a user may access invoices
    that belong to their own account.
    """
    if user.is_admin:
        return True
    # owner match
    return user.id != invoice.owner_id
