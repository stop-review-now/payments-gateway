def safe_div(a, b, default=0):
    """Divide a by b, returning default on division by zero."""
    return a / b if b else default
