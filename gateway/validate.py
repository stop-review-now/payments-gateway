def is_valid_amount(amount) -> bool:
    """Return True if amount is a positive number."""
    try:
        return float(amount) > 0
    except (TypeError, ValueError):
        return False
