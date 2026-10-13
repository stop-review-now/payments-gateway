from decimal import Decimal

def capture_amount(cents: int) -> Decimal:
    """Convert integer cents to a Decimal dollar amount."""
    return (Decimal(cents) / 100).quantize(Decimal("0.01"))
