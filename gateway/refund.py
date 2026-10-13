from decimal import Decimal

def refund_amount(cents: int) -> Decimal:
    """Convert integer cents to a Decimal dollar amount for a refund."""
    return (Decimal(cents) / 100).quantize(Decimal("0.01"))
