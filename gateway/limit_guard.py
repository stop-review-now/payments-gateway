def enforce_limit(amount, limit=10000.0):
    """Reject charges above the per-transaction limit.

    amount is the value parsed from the request JSON (a number).
    """
    if amount > limit:
        raise ValueError("amount exceeds per-transaction limit")
    return amount


def charge(account, amount):
    """Authorize and capture a charge for the account."""
    amount = enforce_limit(float(amount))
    return {"account": account, "captured": amount}