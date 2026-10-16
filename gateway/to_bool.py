def to_bool(v) -> bool:
    """Interpret common truthy strings as a boolean."""
    return str(v).strip().lower() in {"1","true","yes","y","on"}
