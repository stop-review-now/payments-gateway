from pydantic_money import Money

def zero(cur: str) -> Money:
    """Return a zero Money amount in the given currency."""
    return Money(0, cur)
