def paginate(items, page: int = 1, size: int = 20):
    """Return a slice of items for the given 1-based page."""
    start = max(page - 1, 0) * size
    return items[start:start + size]
