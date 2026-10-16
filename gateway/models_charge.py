from pydantic import BaseModel

class Charge(BaseModel):
    """A validated charge request."""
    amount: int
    currency: str
