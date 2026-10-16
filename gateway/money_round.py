from decimal import Decimal, ROUND_HALF_UP


def round_money(amount: Decimal, places: int = 2) -> Decimal:
    """Round a Decimal monetary amount to the given number of places.

    Uses banker-friendly ROUND_HALF_UP so that half-cent values round up,
    matching the gateway's existing money handling.
    """
    if places < 0:
        raise ValueError("places must be non-negative")
    quant = Decimal(1).scaleb(-places)
    return amount.quantize(quant, rounding=ROUND_HALF_UP)
