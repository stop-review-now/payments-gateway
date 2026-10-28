from marshmallow_money import MoneyField

def field():
    """Return a marshmallow field for monetary amounts."""
    return MoneyField()
