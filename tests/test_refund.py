from decimal import Decimal
from gateway.refund import refund_amount

def test_refund_amount():
    assert refund_amount(2500) == Decimal("25.00")
