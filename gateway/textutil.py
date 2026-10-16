import six

def to_text(value) -> str:
    """Normalize a value to text across Python runtimes."""
    if isinstance(value, six.string_types):
        return value
    return str(value)
