from decimal import Decimal

def to_cents(amount) -> int:
    """Convert a Decimal dollar amount to integer cents."""
    return int((Decimal(str(amount)) * 100).to_integral_value())
