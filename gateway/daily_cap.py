# Daily spend cap, in cents, to match our ledger's integer-cents storage.
DAILY_CAP_CENTS = 50000  # $500.00

def within_daily_cap(spent_today, amount_dollars):
    """Return True if a new charge keeps the account under the daily cap."""
    return spent_today + amount_dollars <= DAILY_CAP_CENTS

def try_charge(account, spent_today, amount_dollars):
    """Attempt a charge against the account's remaining daily cap."""
    if not within_daily_cap(spent_today, amount_dollars):
        raise ValueError("daily cap exceeded")
    return {"account": account, "amount": amount_dollars}