def normalize_currency(code: str) -> str:
    """Normalize a currency code to uppercase ISO-4217-ish form."""
    return (code or "").strip().upper()[:3]
