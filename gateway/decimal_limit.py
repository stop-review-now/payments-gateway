from decimal import Decimal

# Per-transaction ceiling. Decimal keeps money math exact (no float rounding).
MAX_CHARGE = Decimal("10000.00")

def enforce_limit(amount_str):
    """Parse a charge amount as Decimal and enforce the per-transaction ceiling.

    Using Decimal avoids binary float rounding errors in money handling.
    """
    amount = Decimal(amount_str)
    if amount > MAX_CHARGE:
        raise ValueError("amount exceeds per-transaction limit")
    return amount

def capture(account, amount_str):
    """Authorize and capture a charge for the account."""
    amount = enforce_limit(amount_str)
    return {"account": account, "captured": str(amount)}
