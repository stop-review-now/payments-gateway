def clamp(value, low, high):
    """Clamp value into the inclusive [low, high] range."""
    return max(low, min(value, high))
