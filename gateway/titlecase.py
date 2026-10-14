def title_case(text: str) -> str:
    """Capitalize the first letter of each word."""
    return " ".join(w.capitalize() for w in text.split())
