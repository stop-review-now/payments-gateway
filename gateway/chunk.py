def chunk(items, size: int):
    """Yield successive lists of at most `size` items."""
    for i in range(0, len(items), size):
        yield items[i:i + size]
